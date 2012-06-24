Summary:	A GPL sound font editor
Name:		smurf
Version:	0.49.1
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Group(pl):	X11/Aplikacje/D�wi�k
URL:		http://smurf.sourceforge.net
Vendor:		Josh Green <jgreen@users.sourceforge.net>
Source0:	http://download.sourceforge.net/smurf/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRequires:	audiofile-devel
BuildRequires:	gtk+-devel
BuildRoot:	/tmp/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Smurf is a GTK based sound font editor. Sound font files are a collection
of audio samples and other data that describe instruments for wavetable
sound cards. Smurf currently supports the AWE 32/64 and has limited support
for the GUS/SoftOSS driver which can use any OSS supported 16 bit sound
card.

%description -l pl
Smurf to edytor "font�w d�wi�kowych" oparty na bibliotece GTK. Pliki
"font�w" s� zbiorem pr�bek d�wi�k�w po��czonych z dodatkowymi danymi, kt�re
razem opisuj� instrumenty dla kart d�wi�kowych wykorzystuj�cych wavetable.
Smurf aktualnie obs�uguje karty AWE 32/64, ma tak�e ograniczone wsparcie
dla sterownik�w GUS/SoftOSS, kt�re mog� wykorzystywa� dowoln� 16 bitow�
kart� obs�ugiwan� przez OSS.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/smurf
