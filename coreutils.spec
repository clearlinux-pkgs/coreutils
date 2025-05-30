#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v24
# autospec commit: a88ffdc
#
# Source0 file verified with key 0xDF6FD971306037D9 (P@draigBrady.com)
#
Name     : coreutils
Version  : 9.7
Release  : 190
URL      : https://mirrors.kernel.org/gnu/coreutils/coreutils-9.7.tar.gz
Source0  : https://mirrors.kernel.org/gnu/coreutils/coreutils-9.7.tar.gz
Source1  : https://mirrors.kernel.org/gnu/coreutils/coreutils-9.7.tar.gz.sig
Source2  : DF6FD971306037D9.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: coreutils-bin = %{version}-%{release}
Requires: coreutils-info = %{version}-%{release}
Requires: coreutils-libexec = %{version}-%{release}
Requires: coreutils-license = %{version}-%{release}
Requires: coreutils-locales = %{version}-%{release}
Requires: coreutils-man = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : acl-staticdev
BuildRequires : attr-dev
BuildRequires : attr-staticdev
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : glibc-locale
BuildRequires : glibc-staticdev
BuildRequires : gmp-dev
BuildRequires : gnupg
BuildRequires : libcap-dev
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-df-test-Do-not-attempt-to-use-the-local-disks-during.patch

%description
These are the GNU core utilities.  This package is the union of
the GNU fileutils, sh-utils, and textutils packages.

%package bin
Summary: bin components for the coreutils package.
Group: Binaries
Requires: coreutils-libexec = %{version}-%{release}
Requires: coreutils-license = %{version}-%{release}

%description bin
bin components for the coreutils package.


%package info
Summary: info components for the coreutils package.
Group: Default

%description info
info components for the coreutils package.


%package libexec
Summary: libexec components for the coreutils package.
Group: Default
Requires: coreutils-license = %{version}-%{release}

%description libexec
libexec components for the coreutils package.


%package license
Summary: license components for the coreutils package.
Group: Default

%description license
license components for the coreutils package.


%package locales
Summary: locales components for the coreutils package.
Group: Default

%description locales
locales components for the coreutils package.


%package man
Summary: man components for the coreutils package.
Group: Default

%description man
man components for the coreutils package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) DF6FD971306037D9' gpg.status
%setup -q -n coreutils-9.7
cd %{_builddir}/coreutils-9.7
%patch -P 1 -p1
pushd ..
cp -a coreutils-9.7 buildavx2
popd

%build
## build_prepend content
CFLAGS="$CFLAGS -static"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744233989
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-no-install-program=kill,groups \
--enable-single-binary=symlinks \
--enable-static \
--enable-single-binary-exceptions=id
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
CFLAGS="$CFLAGS -static"
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-no-install-program=kill,groups \
--enable-single-binary=symlinks \
--enable-static \
--enable-single-binary-exceptions=id
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1744233989
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/coreutils
cp %{_builddir}/coreutils-%{version}/COPYING %{buildroot}/usr/share/package-licenses/coreutils/31a3d460bb3c7d98845187c716a30db81c44b615 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang coreutils
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/coreutils
/V3/usr/bin/id
/usr/bin/[
/usr/bin/b2sum
/usr/bin/base32
/usr/bin/base64
/usr/bin/basename
/usr/bin/basenc
/usr/bin/cat
/usr/bin/chcon
/usr/bin/chgrp
/usr/bin/chmod
/usr/bin/chown
/usr/bin/chroot
/usr/bin/cksum
/usr/bin/comm
/usr/bin/coreutils
/usr/bin/cp
/usr/bin/csplit
/usr/bin/cut
/usr/bin/date
/usr/bin/dd
/usr/bin/df
/usr/bin/dir
/usr/bin/dircolors
/usr/bin/dirname
/usr/bin/du
/usr/bin/echo
/usr/bin/env
/usr/bin/expand
/usr/bin/expr
/usr/bin/factor
/usr/bin/false
/usr/bin/fmt
/usr/bin/fold
/usr/bin/head
/usr/bin/hostid
/usr/bin/id
/usr/bin/install
/usr/bin/join
/usr/bin/link
/usr/bin/ln
/usr/bin/logname
/usr/bin/ls
/usr/bin/md5sum
/usr/bin/mkdir
/usr/bin/mkfifo
/usr/bin/mknod
/usr/bin/mktemp
/usr/bin/mv
/usr/bin/nice
/usr/bin/nl
/usr/bin/nohup
/usr/bin/nproc
/usr/bin/numfmt
/usr/bin/od
/usr/bin/paste
/usr/bin/pathchk
/usr/bin/pinky
/usr/bin/pr
/usr/bin/printenv
/usr/bin/printf
/usr/bin/ptx
/usr/bin/pwd
/usr/bin/readlink
/usr/bin/realpath
/usr/bin/rm
/usr/bin/rmdir
/usr/bin/runcon
/usr/bin/seq
/usr/bin/sha1sum
/usr/bin/sha224sum
/usr/bin/sha256sum
/usr/bin/sha384sum
/usr/bin/sha512sum
/usr/bin/shred
/usr/bin/shuf
/usr/bin/sleep
/usr/bin/sort
/usr/bin/split
/usr/bin/stat
/usr/bin/stdbuf
/usr/bin/stty
/usr/bin/sum
/usr/bin/sync
/usr/bin/tac
/usr/bin/tail
/usr/bin/tee
/usr/bin/test
/usr/bin/timeout
/usr/bin/touch
/usr/bin/tr
/usr/bin/true
/usr/bin/truncate
/usr/bin/tsort
/usr/bin/tty
/usr/bin/uname
/usr/bin/unexpand
/usr/bin/uniq
/usr/bin/unlink
/usr/bin/uptime
/usr/bin/users
/usr/bin/vdir
/usr/bin/wc
/usr/bin/who
/usr/bin/whoami
/usr/bin/yes

%files info
%defattr(0644,root,root,0755)
/usr/share/info/coreutils.info

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/coreutils/libstdbuf.so
/usr/libexec/coreutils/libstdbuf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/coreutils/31a3d460bb3c7d98845187c716a30db81c44b615

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/b2sum.1
/usr/share/man/man1/base32.1
/usr/share/man/man1/base64.1
/usr/share/man/man1/basename.1
/usr/share/man/man1/basenc.1
/usr/share/man/man1/cat.1
/usr/share/man/man1/chcon.1
/usr/share/man/man1/chgrp.1
/usr/share/man/man1/chmod.1
/usr/share/man/man1/chown.1
/usr/share/man/man1/chroot.1
/usr/share/man/man1/cksum.1
/usr/share/man/man1/comm.1
/usr/share/man/man1/coreutils.1
/usr/share/man/man1/cp.1
/usr/share/man/man1/csplit.1
/usr/share/man/man1/cut.1
/usr/share/man/man1/date.1
/usr/share/man/man1/dd.1
/usr/share/man/man1/df.1
/usr/share/man/man1/dir.1
/usr/share/man/man1/dircolors.1
/usr/share/man/man1/dirname.1
/usr/share/man/man1/du.1
/usr/share/man/man1/echo.1
/usr/share/man/man1/env.1
/usr/share/man/man1/expand.1
/usr/share/man/man1/expr.1
/usr/share/man/man1/factor.1
/usr/share/man/man1/false.1
/usr/share/man/man1/fmt.1
/usr/share/man/man1/fold.1
/usr/share/man/man1/head.1
/usr/share/man/man1/hostid.1
/usr/share/man/man1/id.1
/usr/share/man/man1/install.1
/usr/share/man/man1/join.1
/usr/share/man/man1/link.1
/usr/share/man/man1/ln.1
/usr/share/man/man1/logname.1
/usr/share/man/man1/ls.1
/usr/share/man/man1/md5sum.1
/usr/share/man/man1/mkdir.1
/usr/share/man/man1/mkfifo.1
/usr/share/man/man1/mknod.1
/usr/share/man/man1/mktemp.1
/usr/share/man/man1/mv.1
/usr/share/man/man1/nice.1
/usr/share/man/man1/nl.1
/usr/share/man/man1/nohup.1
/usr/share/man/man1/nproc.1
/usr/share/man/man1/numfmt.1
/usr/share/man/man1/od.1
/usr/share/man/man1/paste.1
/usr/share/man/man1/pathchk.1
/usr/share/man/man1/pinky.1
/usr/share/man/man1/pr.1
/usr/share/man/man1/printenv.1
/usr/share/man/man1/printf.1
/usr/share/man/man1/ptx.1
/usr/share/man/man1/pwd.1
/usr/share/man/man1/readlink.1
/usr/share/man/man1/realpath.1
/usr/share/man/man1/rm.1
/usr/share/man/man1/rmdir.1
/usr/share/man/man1/runcon.1
/usr/share/man/man1/seq.1
/usr/share/man/man1/sha1sum.1
/usr/share/man/man1/sha224sum.1
/usr/share/man/man1/sha256sum.1
/usr/share/man/man1/sha384sum.1
/usr/share/man/man1/sha512sum.1
/usr/share/man/man1/shred.1
/usr/share/man/man1/shuf.1
/usr/share/man/man1/sleep.1
/usr/share/man/man1/sort.1
/usr/share/man/man1/split.1
/usr/share/man/man1/stat.1
/usr/share/man/man1/stdbuf.1
/usr/share/man/man1/stty.1
/usr/share/man/man1/sum.1
/usr/share/man/man1/sync.1
/usr/share/man/man1/tac.1
/usr/share/man/man1/tail.1
/usr/share/man/man1/tee.1
/usr/share/man/man1/test.1
/usr/share/man/man1/timeout.1
/usr/share/man/man1/touch.1
/usr/share/man/man1/tr.1
/usr/share/man/man1/true.1
/usr/share/man/man1/truncate.1
/usr/share/man/man1/tsort.1
/usr/share/man/man1/tty.1
/usr/share/man/man1/uname.1
/usr/share/man/man1/unexpand.1
/usr/share/man/man1/uniq.1
/usr/share/man/man1/unlink.1
/usr/share/man/man1/uptime.1
/usr/share/man/man1/users.1
/usr/share/man/man1/vdir.1
/usr/share/man/man1/wc.1
/usr/share/man/man1/who.1
/usr/share/man/man1/whoami.1
/usr/share/man/man1/yes.1

%files locales -f coreutils.lang
%defattr(-,root,root,-)

