Summary:	Tool to check system for binary-hardening
Name:		checksec
Version:	1.5
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	http://www.trapkit.de/tools/%{name}.sh
# Source0-md5:	075996be339ab16ad7b94d6de3ee07bd
Source1:	http://www.trapkit.de/tools/%{name}_changes.txt
# Source1-md5:	03a45df6ac588603c6191dc0a4883531
URL:		http://www.trapkit.de/tools/checksec.html
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
cp -p %{SOURCE1} ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
