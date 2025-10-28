Name:		hyprpwcenter
Version:	0.1.1
Release:	1
Source0:	https://github.com/hyprwm/hyprpwcenter/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	A GUI Pipewire control center
URL:		https://github.com/hyprwm/hyprpwcenter
License:	BSD-3-Clause
Group:		Window Manager/Hyprland
BuildSystem:	cmake

BuildRequires:	cmake
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(hyprtoolkit)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(aquamarine)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(cairo)

%description
A GUI Pipewire control center

%prep
%autosetup -p1

%files
%{_bindir}/%{name}
