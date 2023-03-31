Name:		texlive-logicproof
Version:	33254
Release:	2
Summary:	Box proofs for propositional and predicate logic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/logicproof
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicproof.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicproof.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicproof.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A common style of proof used in propositional and predicate
logic is Fitch proofs, in which each line of the proof has a
statement and a justification, and subproofs within a larger
proof have boxes around them. The package provides environments
for typesetting such proofs and boxes. It creates proofs in a
style similar to that used in "Logic in Computer Science" by
Huth and Ryan.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/logicproof/logicproof.sty
%doc %{_texmfdistdir}/doc/latex/logicproof/README
%doc %{_texmfdistdir}/doc/latex/logicproof/logicproof.pdf
#- source
%doc %{_texmfdistdir}/source/latex/logicproof/logicproof.dtx
%doc %{_texmfdistdir}/source/latex/logicproof/logicproof.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
