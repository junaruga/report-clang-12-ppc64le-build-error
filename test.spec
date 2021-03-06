Name: test
Version: 1
Release: 1%{?dist}
Summary: Test
License: Public Domain
URL: https://github.com/junaruga/report-clang-12-ppc64le-build-error
BuildRequires: clang

%description

%prep
cat > test.cpp <<EOF
#include <complex.h>
int main(void) {
    return 0;
}
EOF

%build
clang --version
clang++ --version

for file in $(find /usr/include/ -name complex.h); do
  rpm -qf "${file}"
done

clang -o test test.cpp
clang++ -o test_cpp test.cpp

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 test %{buildroot}/%{_bindir}/test

%files
%{_bindir}/test

%changelog
* Fri Mar 26 2021 Jun Aruga <jaruga@redhat.com>
- Init.
