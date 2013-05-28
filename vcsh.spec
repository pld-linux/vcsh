Summary:	home directory config manager based on git
Name:		vcsh
Version:	1.3
Release:	0.1
License:	GPL v2
Group:		Applications/Console
Source0:	https://github.com/alerque/vcsh/archive/v%{version}-pld.tar.gz
# Source0-md5:	058289ab41037b9ac8971c63087f5ec0
Patch0:		%{name}-makefile.patch
URL:		https://github.com/RichiH/vcsh
Requires:	mr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} allows you to have several git repositories, all maintaining
their working trees in $HOME without clobbering each other. That, in
turn, means you can have one repository per config set (zsh, vim, ssh,
etc), picking and choosing which configs you want to use on which
machine.

%package -n zsh-completion-%{name}
Summary:	zsh shell completion routines for %{name}
Group:		Applications/Console
Requires:	zsh

%description -n zsh-completion-%{name}
Tab completion routines for %{name} in zsh.

%prep
%setup -q -n %{name}-%{version}-pld
%patch0 -p1

patch -p1 < pld/patches/precompiled_manpage.patch

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
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n zsh-completion-%{name}
%defattr(644,root,root,755)
%{_datadir}/zsh/site-functions/_%{name}
