%define name rox-oroborox
%define version 0.9.7.9
%define release %mkrel 8
%define oname OroboROX

Summary: Window Manager for the ROX desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://roxos.sunsite.dk/dev-contrib/guido/%{oname}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/Other
Url: http://roscidus.com/desktop/OroboROX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libsm-devel
BuildRequires: libxrandr-devel
BuildRequires: libxinerama-devel
BuildRequires: libxext-devel
BuildRequires: libxrender-devel
BuildRequires: libxxf86vm-devel
BuildRequires: xft2-devel
BuildRequires: xpm-devel
BuildRequires: glib2-devel
Requires: rox-lib >= 1.9.13

%description
OroboROX is a small yet fully featured window manager with the ROX Desktop
in mind. OroboROX is based on Oroborus and at this point (version 0.8.2) mostly
identical with its version 2.0.13.


%prep
%setup -q -n %oname
# -n %oname-%version%pre
chmod -R go+r *
chmod 644 Configure/OroboScheme/icon-template.svg


%build
export CC="gcc -L%_prefix/X11R6/lib"
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot{%_libdir/apps,%_bindir,%{_sysconfdir}/X11/wmsession.d}
cp -r ../%oname %buildroot%_libdir/apps/%oname
rm -rf %buildroot%_libdir/apps/%oname/src %buildroot%_libdir/apps/%oname/=build %buildroot%_libdir/apps/%oname/Messages/dist %buildroot%_libdir/apps/%oname/Messages/*po %buildroot%_libdir/apps/%oname/Messages/tips.py %buildroot%_libdir/apps/%oname/.xvpics %buildroot%_libdir/apps/%oname/.DirIcon_old
cat > %buildroot%_bindir/oroborox << EOF
#!/bin/bash
cd %_libdir/apps/%oname
./AppRun
EOF

#gw no translations in this version
#for gmo in %buildroot%_libdir/apps/%oname/Messages/*.gmo;do
#echo "%lang($(basename $gmo|sed s/.gmo//)) $(echo $gmo|sed s!%buildroot!!)" >> %name.lang
#done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %_libdir/apps/%oname/
#%dir %_libdir/apps/%oname/Messages
%doc %_libdir/apps/%oname/Help
%attr(755,root,root) %_bindir/oroborox
%_libdir/apps/%oname/App*
%_libdir/apps/%oname/default*
%_libdir/apps/%oname/Linux-*
%_libdir/apps/%oname/.DirIcon
%_libdir/apps/%oname/Configure


