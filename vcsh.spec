Summary:	home directory config manager based on git
Name:		vcsh
Version:	1.2.3
Release:	0.2
License:	GPL v2
Group:		Applications/Console
Source0:	https://github.com/alerque/vcsh/archive/v%{version}.tar.gz
# Source0-md5:	67ee98eb5db9a4b112966cc8aac41c11
URL:		https://github.com/RichiH/vcsh
Requires:	mr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vcsh allows you to have several git repositories, all maintaining
their working trees in $HOME without clobbering each other. That, in
turn, means you can have one repository per config set (zsh, vim, ssh,
etc), picking and choosing which configs you want to use on which
machine.

%prep
%setup -q -n %{name}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
