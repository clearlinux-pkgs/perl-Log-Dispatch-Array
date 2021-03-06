#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Dispatch-Array
Version  : 1.003
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Log-Dispatch-Array-1.003.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Log-Dispatch-Array-1.003.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblog-dispatch-array-perl/liblog-dispatch-array-perl_1.003-1.debian.tar.xz
Summary  : 'log events to an array (reference)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Log-Dispatch-Array-license = %{version}-%{release}
Requires: perl-Log-Dispatch-Array-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Class::Data::Inheritable)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(Exception::Class)
BuildRequires : perl(Log::Dispatch::Output)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
This archive contains the distribution Log-Dispatch-Array,
version 1.003:
log events to an array (reference)

%package dev
Summary: dev components for the perl-Log-Dispatch-Array package.
Group: Development
Provides: perl-Log-Dispatch-Array-devel = %{version}-%{release}
Requires: perl-Log-Dispatch-Array = %{version}-%{release}

%description dev
dev components for the perl-Log-Dispatch-Array package.


%package license
Summary: license components for the perl-Log-Dispatch-Array package.
Group: Default

%description license
license components for the perl-Log-Dispatch-Array package.


%package perl
Summary: perl components for the perl-Log-Dispatch-Array package.
Group: Default
Requires: perl-Log-Dispatch-Array = %{version}-%{release}

%description perl
perl components for the perl-Log-Dispatch-Array package.


%prep
%setup -q -n Log-Dispatch-Array-1.003
cd %{_builddir}
tar xf %{_sourcedir}/liblog-dispatch-array-perl_1.003-1.debian.tar.xz
cd %{_builddir}/Log-Dispatch-Array-1.003
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Log-Dispatch-Array-1.003/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Dispatch-Array
cp %{_builddir}/Log-Dispatch-Array-1.003/LICENSE %{buildroot}/usr/share/package-licenses/perl-Log-Dispatch-Array/5534c6bbbfd86787763de9db5162d73674e94d26
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Log-Dispatch-Array/ae2702ce93f23396e87f2f13ccbc1c69d37903c2
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Dispatch::Array.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Log-Dispatch-Array/5534c6bbbfd86787763de9db5162d73674e94d26
/usr/share/package-licenses/perl-Log-Dispatch-Array/ae2702ce93f23396e87f2f13ccbc1c69d37903c2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Log/Dispatch/Array.pm
