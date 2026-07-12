import sys

with open('src/components/PublicationsList.tsx', 'r') as f:
    content = f.read()

# Replace the previous Kaggle link with the NeuralNetworkButton
# The previous link starts with <a href="https://www.kaggle.com/georgeokello/"
# and ends with </a>

old_link = """            <a
              href="https://www.kaggle.com/georgeokello/"
              target="_blank"
              rel="noopener noreferrer"
              className={`group shrink-0 relative inline-flex items-center justify-center px-8 py-4 font-mono text-[10px] uppercase tracking-widest font-semibold transition-all overflow-hidden border ${
                isDark 
                  ? "border-emerald-500/40 text-emerald-400 hover:text-emerald-300" 
                  : "border-emerald-500/60 text-emerald-800 hover:text-emerald-900 bg-white"
              }`}
            >
              <div className={`absolute inset-0 translate-y-full group-hover:translate-y-0 transition-transform duration-300 ease-out ${
                isDark ? "bg-emerald-500/10" : "bg-emerald-100/50"
              }`} />
              <span className="relative flex items-center gap-3">
                View Kaggle Profile
                <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
              </span>
            </a>"""

new_link = """            <NeuralNetworkButton href="https://www.kaggle.com/georgeokello/" isDark={isDark} />"""

content = content.replace(old_link, new_link)

with open('src/components/PublicationsList.tsx', 'w') as f:
    f.write(content)

