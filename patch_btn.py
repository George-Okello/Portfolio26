import sys

with open('src/components/PublicationsList.tsx', 'r') as f:
    content = f.read()

neural_button_code = """
function NeuralNetworkButton({ href, isDark }: { href: string; isDark: boolean }) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className={`group relative inline-flex items-center justify-center px-8 py-4 font-mono text-[10px] uppercase tracking-widest font-semibold overflow-hidden border transition-all duration-500 ${
        isDark 
          ? "border-emerald-500/40 text-emerald-400 hover:text-emerald-300 hover:border-emerald-400" 
          : "border-emerald-600/50 text-emerald-800 hover:text-emerald-900 bg-white hover:border-emerald-600 shadow-sm"
      }`}
    >
      {/* Neural nodes and connecting lines effect */}
      <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none">
        {/* Nodes */}
        <div className={`absolute top-2 left-2 w-1.5 h-1.5 rounded-full ${isDark ? "bg-emerald-400" : "bg-emerald-600"}`}></div>
        <div className={`absolute bottom-2 left-6 w-1 h-1 rounded-full ${isDark ? "bg-emerald-400" : "bg-emerald-600"}`}></div>
        <div className={`absolute top-3 right-8 w-1 h-1 rounded-full ${isDark ? "bg-emerald-400" : "bg-emerald-600"}`}></div>
        <div className={`absolute bottom-2 right-2 w-1.5 h-1.5 rounded-full ${isDark ? "bg-emerald-400" : "bg-emerald-600"}`}></div>
        <div className={`absolute top-1/2 left-1/2 w-1 h-1 rounded-full ${isDark ? "bg-emerald-400" : "bg-emerald-600"}`}></div>
        
        {/* Lines */}
        <div className={`absolute top-2.5 left-2.5 w-4 h-[1px] origin-top-left rotate-45 ${isDark ? "bg-emerald-500/50" : "bg-emerald-600/30"}`}></div>
        <div className={`absolute bottom-2 left-6 w-10 h-[1px] origin-bottom-left -rotate-12 ${isDark ? "bg-emerald-500/50" : "bg-emerald-600/30"}`}></div>
        <div className={`absolute top-3 right-8 w-6 h-[1px] origin-top-right rotate-45 ${isDark ? "bg-emerald-500/50" : "bg-emerald-600/30"}`}></div>
        <div className={`absolute bottom-2 right-2 w-6 h-[1px] origin-bottom-right -rotate-12 ${isDark ? "bg-emerald-500/50" : "bg-emerald-600/30"}`}></div>
        <div className={`absolute top-1/2 left-1/2 w-8 h-[1px] origin-center -translate-x-1/2 -translate-y-1/2 rotate-12 ${isDark ? "bg-emerald-500/50" : "bg-emerald-600/30"}`}></div>
      </div>
      
      {/* Glow effect */}
      <div className={`absolute inset-0 translate-y-full group-hover:translate-y-0 transition-transform duration-500 ease-out ${
        isDark ? "bg-emerald-500/10" : "bg-emerald-100/60"
      }`} />
      
      <span className="relative flex items-center gap-3 z-10">
        <Database className="w-4 h-4" />
        Explore Kaggle Notebooks
        <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
      </span>
    </a>
  );
}
"""

# Insert before PublicationsList
content = content.replace('export default function PublicationsList', neural_button_code + '\nexport default function PublicationsList')

with open('src/components/PublicationsList.tsx', 'w') as f:
    f.write(content)

