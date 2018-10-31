# revision 33254
# category Package
# catalog-ctan /macros/latex/contrib/logicproof
# catalog-date 2014-03-27 18:52:36 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-logicproof
Version:	20180303
Release:	2
Summary:	Box proofs for propositional and predicate logic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/logicproof
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicproof.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicproof.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicproof.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
