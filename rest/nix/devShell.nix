rec {
  shellHook-for = { package, python, nixpkgsRelease }: ''
    export PNAME="${package.pname}";
    export PVERSION="${package.version}";
    export PYVERSION="${python.name}";
    export NIXPKGSRELEASE="${nixpkgsRelease}";
    export PS1="\033[37m[\[\033[01;33m\]\$PNAME-\$PVERSION\033[01;37m|\033[01;32m\]\$PYVERSION\]\033[37m|\[\033[00m\]\[\033[01;34m\]\W\033[37m]\033[31m\$\[\033[00m\] ";
    echo;
    echo -e " \033[37m_     \033[33m_         \033[34m_      \033[36m _        \033[0m";
    echo -e "\033[37m| |   \033[33m(_)       \033[34m| |     \033[36m| |       \033[0m";
    echo -e "\033[37m| |    \033[33m_  \033[32m___ \033[34m__| |\033[35m __ _\033[36m| |_ \033[31m__ _ \033[0m";
    echo -e "\033[37m| |   \033[33m| |\033[32m/ __/\033[34m _\` |\033[35m/ _\` |\033[36m __/\033[31m _\` |\033[35mhttps://github.com/nixos/nixpkgs/$NIXPKGSRELEASE\033[0m";
    echo -e "\033[37m| |___\033[33m| |\033[32m (_\033[34m| (_| |\033[35m (_| |\033[36m |\033[31m| (_| |\033[36mhttps://github.com/rydnr/pythoneda\033[0m";
    echo -e "\033[37m\\_____/\033[33m_|\033[32m\\___\\\\\033[34m__,_|\033[35m\\__,_|\033[36m\\__\\\\\033[31m__,_|\033[37mhttps://github.com/acmsl/licdata\033[0m";
    echo;
    echo " Thank you for using Automated Computing Machinery's licdata SDK.";
    echo;
  '';
  devShell-for = { package, python, pkgs, nixpkgsRelease }:
    pkgs.mkShell {
      buildInputs = [ package ];
      shellHook = shellHook-for { inherit package python nixpkgsRelease; };
    };
}
