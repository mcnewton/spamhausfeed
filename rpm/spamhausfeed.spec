Summary:                spamhausfeed
Name:                   spamhausfeed
Version:                0.3
Release:                1
Group:                  Networking/Mail
License:                GPL v2
Source0:                %{name}-%{version}.tar.gz
BuildArch:              noarch
BuildRoot:              %{_tmppath}/%{name}-%{version}

%description
spamhausfeed - to ship relevant bits of MX logs to spamhaus via Janet - http://www.le.ac.uk/users/mcn4/spamhausfeed/

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 755 -p $RPM_BUILD_ROOT/usr/sbin $RPM_BUILD_ROOT/etc/sysconfig $RPM_BUILD_ROOT/etc/init.d
install -c -m 755 spamhausfeed $RPM_BUILD_ROOT/usr/sbin/spamhausfeed
install -c -m 644 spamhausfeed.conf $RPM_BUILD_ROOT/etc/spamhausfeed.conf
install -c -m 644 rpm/spamhausfeed.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/spamhausfeed
install -c -m 755 rpm/spamhausfeed.init $RPM_BUILD_ROOT/etc/init.d/spamhausfeed

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%files
%defattr(755,root,root,-)
/usr/sbin/spamhausfeed
/etc/init.d/spamhausfeed
%config(noreplace) %attr(644,root,root) /etc/spamhausfeed.conf 
%config(noreplace) %attr(644,root,root) /etc/sysconfig/spamhausfeed

%postun

%changelog
* Fri Aug 16 2013 Ben Charlton <bcc@kent.ac.uk> 0.3-1
 - Initial RPM packaging of spamhausfeed. 

