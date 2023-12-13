{ pkgs, ... }:
{
  home.packages = with pkgs; [
    _1password-gui
    qgis-ltr
    slack
    # vpv      # OpenGL issue
    ctop     # terminfo issue?
    dive
    act
  ];

  # `awscli` seems very long to install, disabling for now
  # programs.awscli.enable = true;

  # Easy switching between different AWS profiles using `assume`
  programs.granted.enable = true;

  services.gnome-keyring = {
    enable = true;
    components = ["pkcs11" "secrets" "ssh"];
  };
  services.ssh-agent.enable = true;
}
