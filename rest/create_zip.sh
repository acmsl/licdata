#!/usr/bin/env dry-wit
# Copyright 2024-today Automated Computing Machinery S.L.
# Distributed under the terms of the GNU General Public License v3

DW.import file
DW.import rpm
DW.import curl

# fun: main
# api: public
# txt: Main logic. Gets called by dry-wit.
# txt: Returns 0/TRUE always, but may exit due to errors.
# use: main
function main() {
  command rm -f "${ZIP_FILE}"
  command sudo rm -rf "${DEPS_FOLDER}"
  command mkdir "${DEPS_FOLDER}"

  if ! prepare_zip_file "${PWD}" "${DEPS_FOLDER}"; then
    local _error="${ERROR}"
    if isNotEmpty "${_error}"; then
      logDebug "${_error}"
    fi
    exitWithErrorCode CANNOT_PREPARE_THE_ZIP_FILE_CONTENTS
  fi

  if ! create_zip_file "${DEPS_FOLDER}" "${ZIP_FILE}"; then
    local _error="${ERROR}"
    if isNotEmpty "${_error}"; then
      logDebug "${_error}"
    fi
    exitWithErrorCode CANNOT_CREATE_THE_ZIP_FILE "${ZIP_FILE}"
  fi

#  if ! create_dockerfile "${DOCKERFILE}" "${DEPS_FOLDER}"; then
#    local _error="${ERROR}"
#    if isNotEmpty "${_error}"; then
#      logDebug "${_error}"
#    fi
#    exitWithErrorCode CANNOT_CREATE_THE_DOCKERFILE "${DOCKERFILE}"
#  fi
}

# fun prepare_zip_file source destination
# api: public
# txt: Prepares the contents of the zip file.
# opt: source: The folder with licdata code.
# opt: destination: The folder used for the zip file.
# txt: Returns 0/TRUE if the operation succeeds; 1/FALSE otherwise.
# use: if prepare_zip_file "${PWD}" "/tmp"; then echo "zip file contents prepared"; fi
function prepare_zip_file() {
  local _source="${1}"
  checkNotEmpty source "${_source}" 1
  local _destination="${2}"
  checkNotEmpty destination "${_destination}" 2

  local -i _rescode=${FALSE}

  logInfo -n "Preparing the zip file"
  if copy_nix_modules "${_destination}" \
    && copy_native_libraries "${_destination}" \
    && copy_licdata_files "${_source}" "${_destination}"; then
  # if copy_licdata_files "${_source}" "${_destination}"; then
    _rescode=${TRUE}
    logInfoResult SUCCESS "done"
  else
    logInfoResult FAILURE "failed"
  fi

  return ${_rescode}
}

# fun: copy_nix_modules destination
# api: public
# txt: Copies the pythoneda files to given folder.
# opt: destination: The folder used for the zip file.
# txt: Returns 0/TRUE if the operation succeeds; 1/FALSE otherwise.
# use: if copy_nix_modules "/tmp"; then echo "nix modules copied"; fi
function copy_nix_modules() {
  local _destination="${1}"
  checkNotEmpty destination "${_destination}" 1

  local -i _rescode=${FALSE}
  local _output
  local _module
  local _package

  local _oldIFS="${IFS}"
  IFS="${DWIFS}"
  for _module in $(command echo "${PYTHONPATH}" | command sed 's : \n g' | command grep -v -e '^\.$' | command grep -v -e '/lib-dynload$' | command tac | command tail -n +3); do
    IFS="${_oldIFS}"
    if command pushd "${_module}" > /dev/null 2>&1; then
      IFS="${DWIFS}"
      for _package in $(command find . -maxdepth 1 -type d | command grep -v -e '^\.$' | command grep -v './.git' | command sed 's ./  g'); do
        IFS="${_oldIFS}"
        if fileExists "${_package}/__init__.py"; then
          _output="$(command rsync -avz "${_package}" "${_destination}"/ || echo "$$.ERROR.$$")"
          if isNotEmpty "${_output}" && contains "${_output}" "$$.ERROR.$$"; then
            _rescode=${FALSE}
            break
          else
            _rescode=${TRUE}
          fi
        fi
      done
      IFS="${_oldIFS}"
      if ! command popd > /dev/null 2>&1; then
        _rescode=${FALSE}
        break
      fi
    fi
  done
  IFS="${_oldIFS}"

  return ${_rescode}
}

# fun: copy_licdata_files licdataFolder destination
# api: public
# txt: Copies licdata files to the destination.
# opt: licdataFolder: The folder with licdata code.
# opt: destination: The folder used for the zip file.
# txt: Returns 0/TRUE if the operation succeeds; 1/FALSE otherwise.
# use: if copy_licdata_files "${PWD}" "/tmp"; then echo "licdata files copied"; fi
function copy_licdata_files() {
  local _licdataFolder="${1}"
  checkNotEmpty licdataFolder "${_licdataFolder}" 1
  local _destination="${2}"
  checkNotEmpty destination "${_destination}" 2

  local -i _rescode=${TRUE}
  local _asset
  local _output

  local _oldIFS="${IFS}"
  IFS="${DWIFS}"
  for _asset in org host.json requirements.txt CreateClient; do
    IFS="${_oldIFS}"
    _output="$(command cp -r "${_licdataFolder}/${_asset}" "${_destination}"/ || echo "$$.ERROR.$$")"
    if isNotEmpty "${_output}" && contains "${_output}" "$$.ERROR.$$"; then
      _rescode=${FALSE}
      break
    fi
  done
  IFS="${_oldIFS}"

  return ${_rescode}
}

# fun: copy_native_libraries folder
# api: public
# txt: Downloads and copies native libraries to given folder.
# opt: folder: The destination folder.
# txt: Returns 0/TRUE if the operation succeeds; 1/FALSE otherwise.
# use: if copy_native_libraries /tmp/; then echo "Libraries copied"; fi
function copy_native_libraries() {
  local _folder="${1}"
  checkNotEmpty folder "${_folder}" 1

  local -i _rescode=${TRUE}

  local _url
  local _oldIFS="${IFS}"
  IFS="${DWIFS}"
  for _url in ${LIBSSL3_RPM_URL}; do
    IFS="${_oldIFS}"
    if ! copy_native_library "${_url}" "${_folder}"; then
      _rescode=${FALSE}
      break
    fi
  done
  IFS="${_oldIFS}"

  return ${_rescode}
}

# fun: copy_native_library url folder
# api: public
# txt: Downloads and copies a native library to given folder.
# opt: url: The url of the library.
# opt: folder: The destination folder.
# txt: Returns 0/TRUE if the operation succeeds; 1/FALSE otherwise.
# use: if copy_native_library "https://example.com/sample.rpm" /tmp/; then echo "Library downloaded and copied"; fi
function copy_native_library() {
  local _url="${1}"
  checkNotEmpty url "${_url}" 1
  local _folder="${2}"
  checkNotEmpty folder "${_folder}" 2

  local -i _rescode=${FALSE}

  local _destination="${_folder}/.$$"
  local _rpmFile="${_destination}/.temp.rpm"
  mkdir -p "${_destination}"
  if curlDownload "${_url}" "${_rpmFile}" \
    && extractRpm "${_rpmFile}" "${_destination}"; then
    find "${_destination}/usr/lib64" -name '*.so*' -exec cp {} "${_folder}" \;
    _rescode=$?
  fi
  rm -rf "${_destination}"

  return ${_rescode}
}

# fun: create_zip_file zipFile
# api: public
# txt: Creates the zip file.
# opt: zipFile: The zip file to create.
# txt: Returns 0/TRUE if the file could be created; 1/FALSE otherwise.
# use: if create_zip_file /tmp/myfile.zip; then echo "file created"; fi
function create_zip_file() {
  local _folder="${1}"
  checkNotEmpty folder "${_folder}" 1
  local _zipFile="${2}"
  checkNotEmpty zipFile "${_zipFile}" 2

  local -i _rescode
  local _output

  logDebug -n "Creating ${_zipFile}"
  _output="$(command pushd "${_folder}" > /dev/null 2>&1 && command zip -r "${_zipFile}" . && command popd > /dev/null 2>&1 || echo "$$.ERROR.$$")"
  if isNotEmpty "${_output}" && contains "${_output}" "$$.ERROR.$$"; then
    logDebugResult FAILURE "failed"
    _rescode=${FALSE}
  else
    logDebugResult SUCCESS "done"
    _rescode=${TRUE}
  fi

  return ${_rescode}
}

# fun: create_dockerfile dockerfile
# api: public
# txt: Creates the Dockerfile
# opt: dockerfile: The output file.
# opt: depsFolder: The dependencies folder.
# txt: Returns 0/TRUE if the file could be created; 1/FALSE otherwise.
# use: if create_dockerfile ~/Dockerfile ~/.deps; then
# use:   echo "Dockerfile created"
# use: fi
function create_dockerfile() {
  local _dockerfile="${1}"
  checkNotEmpty dockerfile "${_dockerfile}" 1
  local _depsFolder="${2}"
  checkNotEmpty depsFolder "${_depsFolder}" 2
  _depsFolder="$(basename "${_depsFolder}")"

  local -i _rescode=${FALSE}

  cat <<EOF > "${_dockerfile}"
FROM mcr.microsoft.com/azure-functions/python:4-python3.11

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    libssl-dev \
    && apt-get clean

# Set the working directory
WORKDIR /home/site/wwwroot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .deps/* .

# Expose the Azure Functions runtime port
ENV FUNCTIONS_WORKER_RUNTIME python

EOF

  _rescode=$?

  return ${_rescode}
}

## Script metadata and CLI settings.
setScriptDescription "Packages the rest.zip file"
setScriptLicenseSummary "Distributed under the terms of the GNU General Public License v3"
setScriptCopyright "Copyleft 2024-today Automated Computing Machinery S.L."

addCommandLineFlag "zipFile" "z" "The full path to the zip file" MANDATORY EXPECTS_ARGUMENT
addCommandLineFlag "dockerfile" "d" "The full path to the Dockerfile" MANDATORY EXPECTS_ARGUMENT

checkReq zip
checkReq grep
checkReq sed
checkReq tac
checkReq tail

addError CANNOT_CREATE_A_TEMPORARY_FOLDER "Cannot create a temporary folder"
addError CANNOT_PREPARE_THE_ZIP_FILE_CONTENTS "Cannot prepare the zip file contents"
addError CANNOT_CREATE_THE_ZIP_FILE "Cannot create the zip file "
addError CANNOT_CREATE_THE_DOCKERFILE "Cannot create the Dockerfile"

defineEnvVar LIBSSL3_RPM_URL MANDATORY "The url of libssl rpm" "https://rpmfind.net/linux/epel/8/Everything/x86_64/Packages/o/openssl3-libs-3.2.2-2.1.el8.x86_64.rpm"
defineEnvVar DEPS_FOLDER MANDATORY "The absolute path of the folder to copy the Python dependencies" "${PWD}/.deps"
# vim: syntax=sh ts=2 sw=2 sts=4 sr noet
