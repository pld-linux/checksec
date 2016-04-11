Summary:	Tool to check system for binary-hardening
Name:		checksec
Version:	1.7.4
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://github.com/slimm609/checksec.sh/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8e963bc27f58d14c9b3657600a5c298e
URL:		https://github.com/slimm609/checksec.sh
Requires:	binutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modern Linux distributions offer some mitigation techniques to make it
harder to exploit software vulnerabilities reliably. Mitigations such
as RELRO, NoExecute (NX), Stack Canaries, Address Space Layout
Randomization (ASLR) and Position Independent Executables (PIE) have
made reliably exploiting any vulnerabilities that do exist far more
challenging.

The checksec script is designed to test what *standard* Linux OS and
PaX <http://pax.grsecurity.net/> security features are being used.

As of version 1.3 the script also lists the status of various Linux
kernel protection mechanisms.

checksec can check binary-files and running processes for hardening
features.

%prep
%setup -qn %{name}.sh-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man7}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p extras/man/checksec.7* $RPM_BUILD_ROOT%{_mandir}/man7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.txt ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man7/checksec.7*
