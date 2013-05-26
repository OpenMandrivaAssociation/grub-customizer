# Basic Information
Name: grub-customizer
Version: 3.0.4
Release: 1
Summary: Graphical interface to configure the grub2/burg settings
Group: System/Configuration/Boot and Init
License: GPLv3
URL: https://launchpad.net/grub-customizer

# Source Information
Source0: %{name}_%{version}.tar.gz
Source1: %{name}-grub.cfg
Source2: %{name}-pamd
Patch0: %{name}-sbin.patch

# Dependency Information
BuildRequires: cmake gcc-c++ gtkmm2.4-devel gettext openssl-devel grub2
Requires: grub2

%description
Grub Customizer is a graphical interface to configure the grub2/burg
settings with focus on the individual list order - without losing the
dynamical behavior of grub.

%prep
#%setup -q -c -n %{name}-%{version}
%setup -q
%patch0 -p2

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

%changelog
* Sat May 12 2012 Vladimir Testov <Vladimir.Testov> 2.5.5
- Initial Spec File
