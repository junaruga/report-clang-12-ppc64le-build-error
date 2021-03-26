Name: test
Version: 1
Release: 1%{?dist}
Summary: Test
License: Public Domain
URL: https://github.com/junaruga/report-clang-12-ppc64le-build-error
BuildRequires: clang

%description

%prep
cat > test.c <<EOF
#include <complex.h>
int main(void) {
    int class=0;
    return class;
}
EOF

%build
clang test.c -o test

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 test %{buildroot}/%{_bindir}/test

%files
%{_bindir}/test

%changelog
* Fri Mar 26 2021 Jun Aruga <jaruga@redhat.com>
- Init.
