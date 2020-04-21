from matplotlib.font_manager import FontProperties
import matplotlib 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)  


plt.subplot(111, facecolor='w')

alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}

yp = [0.9,0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2,0.1]
start = -0.9
ypl = len(yp)
mtex = [""]*7
mtex[0] =r'$\alpha > \beta$'#orign
mtex[1] =r'$\alpha_i > \beta_i$'#lower
mtex[2] =r'$\alpha^{ic}>\beta_{ic}$'#upper
mtex[3] =r'$\sum_{i=0}^\infty x_i$'#sum
mtex[4] =r'$\frac{3}{4} \binom{3}{4} \genfrac{}{}{0}{0}{3}{4}$' #排版不同
mtex[5] =r'$\sqrt{2}$' #sqrt
mtex[6] =r'$\sqrt[3]{x}$' #3换成n不行啊
for k, text in enumerate(mtex):
    if text == "":
        continue
    x =  start + 0.2 * (k//ypl)
    t = plt.text( x, yp[k%ypl], text,**alignment)
# new x 
start = x + 0.2
accents=[""] * 13 
accents[0]=r'$\acute a$'
accents[1]=r'$\bar a$'
accents[2]=r'$\breve a$'
accents[3]=r'$\ddot a$'
accents[4]=r'$\dot a$'
accents[5]=r'$\grave a$'
accents[6]=r'$\hat a$'
accents[7]=r'$\tilde a$'
accents[8]=r'$\vec a$'
accents[9]=r'$\overline{abc} $'
accents[10]=r'$\widehat{abc} $'
accents[11]=r'$\widetilde{abc} $'
accents[12]=r"$\hat i\ \ \hat \imath$"

for k, text in enumerate(accents):
    if text == "":
        continue
    x =  start + 0.2 * (k//ypl)
    t = plt.text( x , yp[k%ypl], text,**alignment)



fonts=[""]*8
fonts[0] = r'$\mathrm{Roman}$'
fonts[1] = r'$\mathit{Italic}$'
fonts[2] = r'$\mathtt{Twriter}$'
#fonts[3] = r'$\mathcal{CAGRAPHY}'#not support
fonts[3] = r'$\mathbb{blackboard}$'
fonts[4] = r'$\mathrm{\mathbb{blackboard}}$'
fonts[5] = r'$\mathfrak{Fraktur}$'
fonts[6] = r'$\mathsf{sansserif}$'
fonts[7] = r'$\mathrm{\mathsf{sansserif}}$'

start = x + 0.2
for k, text in enumerate(fonts):
    if text == "":
        continue
    x =  start + 0.3 * (k//ypl)
    t = plt.text( x , yp[k%ypl], text, **alignment)

lower_case_greek=r"""
α \alpha	β \beta	χ \chi	δ \delta	ϝ \digamma	ε \epsilon
η \eta	γ \gamma	ι \iota	κ \kappa	λ \lambda	μ \mu
ν \nu	ω \omega	ϕ \phi	π \pi	ψ \psi	ρ \rho
σ \sigma	τ \tau	θ \theta	υ \upsilon	ε \varepsilon	ϰ \varkappa
φ \varphi	ϖ \varpi	ϱ \varrho	ς \varsigma	ϑ \vartheta	ξ \xi
ζ \zeta	 
"""
lower_case_greek = [x.strip() for x in lower_case_greek.split()[1::2]]

upper_case_grek=r"""
Δ \Delta	Γ \Gamma	Λ \Lambda	Ω \Omega	Φ \Phi	Π \Pi	Ψ \Psi	Σ \Sigma
Θ \Theta	Υ \Upsilon	Ξ \Xi	℧ \mho	∇ \nabla
"""
upper_case_grek = [x.strip() for x in upper_case_grek.split()[1::2]]

hebrew=r"""
ℵ \aleph	ℶ \beth	ℸ \daleth	ℷ \gimel	
"""
hebrew = [x.strip() for x in hebrew.split()[1::2]]

delimiters=r"""
/ /	[ [	⇓ \Downarrow	⇑ \Uparrow	‖ \Vert	\backslash
↓ \downarrow	⟨ \langle	⌈ \lceil	⌊ \lfloor	⌞ \llcorner	⌟ \lrcorner
⟩ \rangle	⌉ \rceil	⌋ \rfloor	⌜ \ulcorner	↑ \uparrow	⌝ \urcorner
\vert   { \{	| \| } \}	] ]	
"""
delimiters = [x.strip() for x in delimiters.split()[1::2]]

miscellaneous=r"""
$ \$	Å \AA	Ⅎ \Finv	⅁ \Game
ℑ \Im	¶ \P	ℜ \Re	§ \S
∠ \angle	‵ \backprime	★ \bigstar	■ \blacksquare
▴ \blacktriangle	▾ \blacktriangledown	⋯ \cdots	✓ \checkmark
® \circledR	Ⓢ \circledS	♣ \clubsuit	∁ \complement
© \copyright	⋱ \ddots	♢ \diamondsuit	ℓ \ell
∅ \emptyset	ð \eth	∃ \exists	♭ \flat
∀ \forall	ħ \hbar	♡ \heartsuit	ℏ \hslash
∭ \iiint	∬ \iint	ı \imath	∞ \infty
ȷ \jmath	… \ldots	∡ \measuredangle	♮ \natural
¬ \neg	∄ \nexists	∰ \oiiint	∂ \partial
′ \prime	♯ \sharp	♠ \spadesuit	∢ \sphericalangle
ß \ss	▿ \triangledown	∅ \varnothing	▵ \vartriangle
⋮ \vdots	℘ \wp	¥ \yen
"""
miscellaneous=[x.strip() for x in miscellaneous.split()[1::2]]

symbols = lower_case_greek + upper_case_grek + hebrew + delimiters + miscellaneous
start = x + 0.3
for k, text in enumerate(symbols):
    if text == "":
        continue
    x =  start + 0.2 * (k//ypl)
    t = plt.text( x , yp[k%ypl], f"${text}$", **alignment)

plt.axis([-1, 3, 0, 1])

plt.show()