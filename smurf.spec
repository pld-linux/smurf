Summary:	A GPL sound font editor
Name:		smurf
Version:	0.49.8
Release:	1
License:	GPL
Vendor:		Josh Green <jgreen@users.sourceforge.net>
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	ftp://download.sourceforge.net/pub/sourceforge/smurf/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://smurf.sourceforge.net/
BuildRequires:	audiofile-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Smurf is a GTK based sound font editor. Sound font files are a
collection of audio samples and other data that describe instruments
for wavetable sound cards. Smurf currently supports the AWE 32/64 and
has limited support for the GUS/SoftOSS driver which can use any OSS
supported 16 bit sound card.

%description -l pl
Smurf to edytor "fontów d¼wiêkowych" oparty na bibliotece GTK. Pliki
"fontów" s± zbiorem próbek d¼wiêków po³±czonych z dodatkowymi danymi,
które razem opisuj± instrumenty dla kart d¼wiêkowych wykorzystuj±cych
wavetable. Smurf aktualnie obs³uguje karty AWE 32/64, ma tak¿e
ograniczone wsparcie dla sterowników GUS/SoftOSS, które mog±
wykorzystywaæ dowoln± 16 bitow± kartê obs³ugiwan± przez OSS.

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

gzip -9nf AUTHORS NEWS README ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/smurf
%{_applnkdir}/Multimedia/*
