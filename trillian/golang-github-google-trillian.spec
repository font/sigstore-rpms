# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/google/trillian
%global goipath         github.com/google/trillian
Version:                1.4.0

%gometa

%global common_description %{expand:
A transparent, highly scalable and cryptographically verifiable data store.}

%global gobinaries      trillian_log_server trillian_log_signer
%global golicenses      LICENSE
%global godocs          docs examples CONTRIBUTING.md AUTHORS README.md\\\
                        CHANGELOG.md CONTRIBUTORS PULL_REQUEST_TEMPLATE.md\\\
                        extension/README.md integration/README.md\\\
                        experimental/batchmap/README.md quota/etcd/README.md\\\
                        deployment/README.md storage/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A transparent, highly scalable and cryptographically verifiable data store

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Requires:       mariadb-server

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for f in %{gobinaries}; do
  %gobuild -o %{gobuilddir}/bin/$f %{goipath}/cmd/$f
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# Disabling tests that rely on database server and ones with package import
# errors.
%gocheck -d client/rpcflags \
         -d experimental/batchmap \
         -d integration/quota \
         -t quota/etcd \
         -d storage/testdb \
         -t testonly/integration \
         -t util/election2/etcd
%endif

%files
%license LICENSE
%doc docs examples CONTRIBUTING.md AUTHORS README.md CHANGELOG.md CONTRIBUTORS
%doc extension/README.md integration/README.md
%doc experimental/batchmap/README.md quota/etcd/README.md deployment/README.md
%doc storage/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Apr 14 2022 Ivan Font <ifont@redhat.com> - 1.4.0-1
- Initial package
