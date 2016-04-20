Summary:	Graphical interface to configure the grub2/burg settings
Name:		grub-customizer
Version:	5.0.5
Release:	0.1
License:	GPLv3+
Group:		System/Configuration/Boot and Init
Url:		https://launchpad.net/grub-customizer
Source0:	https://launchpadlibrarian.net/160721885/%{name}_%{version}.tar.gz
Source1:	%{name}-grub.cfg
Source2:	%{name}-pamd
Patch0:		grub-customizer-sbin.patch
Patch1:		grub-customizer-3.0.4-russian_desktopfile.patch
BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	grub2
Requires:	grub2
Requires:	usermode-consoleonly

%description
Grub Customizer is a graphical interface to configure the grub2/burg
settings with focus on the individual list order - without losing the
dynamical behavior of grub.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/polkit-1/actions/*.policy
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_libdir}/grubcfg-proxy
%{_mandir}/man1/%{name}.1*
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/grub.cfg
%{_sysconfdir}/pam.d/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p2
%patch1 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_bindir}
ln -s consolehelper %{buildroot}%{_bindir}/%{name}

mkdir %{buildroot}/etc/%{name} -p
cp %{SOURCE1} %{buildroot}/etc/%{name}/grub.cfg
mkdir %{buildroot}/etc/pam.d -p
cp %{SOURCE2} %{buildroot}/etc/pam.d/%{name}

%find_lang %{name}

