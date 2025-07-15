Summary:	A GPL sound font editor
Summary(pl.UTF-8):	Edytor fontów dźwiękowych
Name:		smurf
Version:	0.52.6
Release:	4
License:	GPL
Vendor:		Josh Green <jgreen@users.sourceforge.net>
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/smurf/%{name}-%{version}.tar.gz
# Source0-md5:	5fafbd7557112f8d3d794a8101075d84
Source1:	%{name}.desktop
Patch0:		%{name}-remove_private_gettext.m4.patch
Patch1:		%{name}-po.patch
URL:		http://smurf.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smurf is a GTK+ based sound font editor. Sound font files are a
collection of audio samples and other data that describe instruments
for wavetable sound cards. Smurf currently supports the AWE 32/64 and
has limited support for the GUS/SoftOSS driver which can use any OSS
supported 16 bit sound card.

%description -l pl.UTF-8
Smurf to edytor "fontów dźwiękowych" oparty na bibliotece GTK+. Pliki
"fontów" są zbiorem próbek dźwięków połączonych z dodatkowymi danymi,
które razem opisują instrumenty dla kart dźwiękowych wykorzystujących
wavetable. Smurf aktualnie obsługuje karty AWE 32/64, ma także
ograniczone wsparcie dla sterowników GUS/SoftOSS, które mogą
wykorzystywać dowolną 16-bitową kartę obsługiwaną przez OSS.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/smurf
%{_desktopdir}/*.desktop
