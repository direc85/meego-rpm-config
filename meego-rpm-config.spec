# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       meego-rpm-config
Summary:    MeeGo specific rpm configuration files
Version:    0.18
Release:    1
Group:      Development/System
License:    GPL+
BuildArch:  noarch
URL:        http://meego.com
Source0:    meego-rpm-config-%{version}.tar.bz2
Source100:  meego-rpm-config.yaml
Patch0:     meego-rpm-config-0.18-merchanges.patch
Patch1:     meego-rpm-config-0.18-bashism.patch
Patch2:     meego-rpm-config-0.18-flexible-install.patch
Patch3:     meego-rpm-config-xzdebuginfo.patch


%description
MeeGo specific rpm configuration files.



%prep
%setup -q -n %{name}-%{version}

# meego-rpm-config-0.18-merchanges.patch
%patch0 -p1
# meego-rpm-config-0.18-bashism.patch
%patch1 -p1
# meego-rpm-config-0.18-flexible-install.patch
%patch2 -p1
# meego-rpm-config-xzdebuginfo.patch
%patch3 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
make DESTDIR=${RPM_BUILD_ROOT} install
# << install post






%files
%defattr(-,root,root,-)
# >> files
%{_prefix}/lib/rpm/meego
# << files


