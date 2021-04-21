let
  unstable = import
    (builtins.fetchTarball https://github.com/NixOS/nixpkgs-channels/archive/nixos-unstable.tar.gz) { };
in
unstable.mkShell {
  buildInputs = [
    unstable.python38Full
    unstable.python38Packages.scrapy
    unstable.python38Packages.python-language-server
  ];
}
