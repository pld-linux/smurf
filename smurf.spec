Summary:	A GPL sound font editor
Name:		smurf
Version:	0.49.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
URL:		http://smurf.sourceforge.net
Vendor:		Josh Green <jgreen@users.sourceforge.net>
Source0:	http://download.sourceforge.net/smurf/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRequires:	audiofile-devel
BuildRequires:	gtk+-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
Smurf is a GTK based sound font editor. Sound font files are a collection
of audio samples and other data that describe instruments for wavetable
sound cards. Smurf currently supports the AWE 32/64 and has limited support
for the GUS/SoftOSS driver which can use any OSS supported 16 bit sound
card.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README COPYING ChangeLog
%attr(755,root,root) %{_bindir}/smurf
