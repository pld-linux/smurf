%define name	smurf
%define version	0.49.1
%define release	1
%define prefix	/usr

Summary: A GPL sound font editor.
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Copyright: GPL
Group: Applications/Multimedia
URL: http://smurf.sourceforge.net
Vendor: Josh Green <jgreen@users.sourceforge.net>
Source: http://download.sourceforge.net/smurf/%{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}

%description
Smurf is a GTK based sound font editor. Sound font files are
a collection of audio samples and other data that describe
instruments for wavetable sound cards. Smurf currently
supports the AWE 32/64 and has limited support for the
GUS/SoftOSS driver which can use any OSS supported 16 bit
sound card.

%prep
%setup -q

%build
./configure --prefix=%{prefix}
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING ChangeLog
%{prefix}/bin/smurf

%changelog
* Sat Mar 25 2000 Josh Green <jgreen@users.sourceforge.net>
- Removed OSS reserved variable initialization in guspatch.c
- Added auto creation of .spec file to configure.in

* Wed Mar 21 2000 Josh Green <jgreen@users.sourceforge.net>
- Faster SF tree with multiple file load capability, sample viewer,
  view/change preset parameters, preferences and other improvements
