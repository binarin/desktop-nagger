{pkgs ? import <nixpkgs> {}}:

with pkgs;

python3Packages.buildPythonPackage rec {
  version = "0.2";
  name = "desktop-nagger-${version}";
  src = ./.;

  nativeBuildInputs = [
    wrapGAppsHook
    gobjectIntrospection
  ];

  buildInputs = [
    gtk3
  ];

  propagatedBuildInputs = [
    python3Packages.pygobject3
  ];

  meta = {
    homepage = http://github.com/binarin/desktop-nagger;
    description = "Displays desktop notifications in an annoying fashion";
    license = stdenv.lib.licenses.mit;
  };
}
