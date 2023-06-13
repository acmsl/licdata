{
  description = "Licdata server";

  inputs = rec {
    nixos.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils/v1.0.0";
    poetry2nix = {
      url = "github:nix-community/poetry2nix/v1.28.0";
      inputs.nixpkgs.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
    };
    pythoneda-base = {
      url = "github:pythoneda/base/0.0.1a11";
      inputs.nixos.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
      inputs.poetry2nix.follows = "poetry2nix";
    };
    pythoneda-infrastructure-base = {
      url = "github:pythoneda-infrastructure/base/0.0.1a6";
      inputs.nixos.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
      inputs.poetry2nix.follows = "poetry2nix";
      inputs.pythoneda-base.follows = "pythoneda-base";
    };
    pythoneda-application-base = {
      url = "github:pythoneda-application/base/0.0.1a6";
      inputs.nixos.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
      inputs.poetry2nix.follows = "poetry2nix";
      inputs.pythoneda-base.follows = "pythoneda-base";
      inputs.pythoneda-infrastructure-base.follows =
        "pythoneda-infrastructure-base";
    };
  };
  outputs = { self, ... }@inputs:
    with inputs;
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixos { inherit system; };
        description = "Licdata server";
        license = pkgs.lib.licenses.gpl3;
        maintainers = with pkgs.lib.maintainers; [ ];
        nixpkgsRelease = "nixos-23.05";
        shared = import ./nix/devShell.nix;
        licdata-server-for = { version, pythoneda-base
          , pythoneda-infrastructure-base, pythoneda-application-base, python }:
          python.pkgs.buildPythonPackage rec {
            pname = "licdata-server";
            inherit version;
            src = ./.;
            format = "pyproject";

            nativeBuildInputs = with python.pkgs; [ pkgs.poetry poetry-core ];

            propagatedBuildInputs = with python.pkgs; [
              pythoneda-base
              pythoneda-infrastructure-base
              pythoneda-application-base
            ];

            checkInputs = with python.pkgs; [ pytest ];

            pythonImportsCheck = [ "domain" "infrastructure" "application" ];

            meta = with pkgs.lib; {
              inherit description license homepage maintainers;
            };
          };
        licdata-server-0_0_1a3-for = { pythoneda-base
          , pythoneda-infrastructure-base, pythoneda-application-base, python }:
          licdata-server-for {
            version = "0.0.1a3";
            inherit pythoneda-base pythoneda-infrastructure-base
              pythoneda-application-base python;
          };
      in rec {
        packages = rec {
          licdata-server-0_0_1a3-python38 = licdata-server-0_0_1a3-for {
            pythoneda-base =
              pythoneda-base.packages.${system}.pythoneda-base-latest-python38;
            pythoneda-infrastructure-base =
              pythoneda-infrastructure-base.packages.${system}.pythoneda-infrastructure-base-latest-python38;
            pythoneda-application-base =
              pythoneda-application-base.packages.${system}.pythoneda-application-base-latest-python38;
            python = pkgs.python38;
          };
          licdata-server-0_0_1a3-python39 = licdata-server-0_0_1a3-for {
            pythoneda-base =
              pythoneda-base.packages.${system}.pythoneda-base-latest-python38;
            pythoneda-infrastructure-base =
              pythoneda-infrastructure-base.packages.${system}.pythoneda-infrastructure-base-latest-python38;
            pythoneda-application-base =
              pythoneda-application-base.packages.${system}.pythoneda-application-base-latest-python38;
            python = pkgs.python38;
          };
          licdata-server-0_0_1a3-python310 = licdata-server-0_0_1a3-for {
            pythoneda-base =
              pythoneda-base.packages.${system}.pythoneda-base-latest-python310;
            pythoneda-infrastructure-base =
              pythoneda-infrastructure-base.packages.${system}.pythoneda-infrastructure-base-latest-python310;
            pythoneda-application-base =
              pythoneda-application-base.packages.${system}.pythoneda-application-base-latest-python310;
            python = pkgs.python310;
          };
          licdata-server-latest-python38 = licdata-server-0_0_1a3-python38;
          licdata-server-latest-python39 = licdata-server-0_0_1a3-python39;
          licdata-server-latest-python310 = licdata-server-0_0_1a3-python310;
          licdata-server-latest = licdata-server-latest-python310;
          default = licdata-server-latest;
        };
        defaultPackage = packages.default;
        devShells = rec {
          licdata-server-0_0_1a3-python38 = shared.devShell-for {
            package = packages.licdata-server-0_0_1a3-python38;
            python = pkgs.python38;
            inherit pkgs nixpkgsRelease;
          };
          licdata-server-0_0_1a3-python39 = shared.devShell-for {
            package = packages.licdata-server-0_0_1a3-python39;
            python = pkgs.python39;
            inherit pkgs nixpkgsRelease;
          };
          licdata-server-0_0_1a3-python310 = shared.devShell-for {
            package = packages.licdata-server-0_0_1a3-python310;
            python = pkgs.python310;
            inherit pkgs nixpkgsRelease;
          };
          licdata-server-latest-python38 = licdata-server-0_0_1a3-python38;
          licdata-server-latest-python39 = licdata-server-0_0_1a3-python39;
          licdata-server-latest-python310 = licdata-server-0_0_1a3-python310;
          licdata-server-latest = licdata-server-latest-python310;
          default = licdata-server-latest;
        };
      });
}
