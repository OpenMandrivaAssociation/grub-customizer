Name:		grub-customizer
Version:	4.0.3
Release:	2
Summary:	Graphical interface to configure the grub2/burg settings
Group:		System/Configuration/Boot and Init
License:	GPLv3
URL:		https://launchpad.net/grub-customizer
Source0:	https://launchpadlibrarian.net/160721885/%{name}_%{version}.tar.gz
Source1:	%{name}-grub.cfg
Source2:	%{name}-pamd
Patch0:		%{name}-sbin.patch
Patch1:		grub-customizer-3.0.4-russian_desktopfile.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	gettext
BuildRequires:	openssl-devel
BuildRequires:	grub2
Requires:	grub2

%description
Grub Customizer is a graphical interface to configure the grub2/burg
settings with focus on the individual list order - without losing the
dynamical behavior of grub.

%prep
#%setup -q -c -n %{name}-%{version}
%setup -q
%patch0 -p2
%patch1 -p1

%build
%cmake
%make

%install
mkdir %{buildroot}/etc/%{name} -p
cp %{SOURCE1} %{buildroot}/etc/%{name}/grub.cfg
mkdir %{buildroot}/etc/pam.d -p
cp %{SOURCE2} %{buildroot}/etc/pam.d/%{name}
cd build
make install DESTDIR=%{buildroot}
cd ..
mkdir %{buildroot}/%{_bindir} -p
ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/%{name}
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/polkit-1/*
%{_mandir}/man1/*
%{_iconsdir}/*
%{_libdir}/*
%{_sysconfdir}/*
%exclude /usr/lib/debug/
