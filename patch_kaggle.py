import sys

with open('src/components/PublicationsList.tsx', 'r') as f:
    content = f.read()

# 1. Update imports
content = content.replace(
    'import { BookOpen, ChevronDown, ChevronUp, ExternalLink, Clock } from "lucide-react";',
    'import { BookOpen, ChevronDown, ChevronUp, ExternalLink, Clock, Database, ArrowRight } from "lucide-react";'
)

# 2. Add Kaggle Banner
kaggle_banner = """
        {/* Kaggle Creative Banner */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-50px" }}
          transition={{ duration: 0.6 }}
          className={`mt-16 md:col-span-2 relative overflow-hidden p-8 md:p-12 border ${
            isDark 
              ? "border-emerald-500/20 bg-gradient-to-r from-emerald-500/10 to-transparent" 
              : "border-emerald-500/30 bg-gradient-to-r from-emerald-50 to-transparent"
          }`}
        >
          <div className="absolute top-0 right-0 p-8 opacity-10 pointer-events-none">
            <div className="w-32 h-32 rounded-full border-4 border-dashed border-emerald-500 animate-[spin_20s_linear_infinite]" />
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="w-16 h-16 rounded-full border-2 border-emerald-500 animate-[spin_15s_linear_infinite_reverse]" />
            </div>
          </div>
          
          <div className="relative z-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
            <div className="max-w-2xl">
              <div className="flex items-center gap-3 mb-4">
                <div className={`p-2 border rounded ${isDark ? "border-emerald-500/30 bg-emerald-500/10" : "border-emerald-300 bg-emerald-100/50"}`}>
                  <Database className={`w-5 h-5 ${isDark ? "text-emerald-400" : "text-emerald-600"}`} />
                </div>
                <span className={`text-[10px] font-mono uppercase tracking-widest font-semibold ${isDark ? "text-emerald-400" : "text-emerald-700"}`}>
                  More Explorations
                </span>
              </div>
              <h4 className="text-2xl font-serif tracking-tight mb-2">Data Science & Competitions</h4>
              <p className="text-sm font-light opacity-80 leading-relaxed">
                While my selected major works are detailed above, I also actively experiment with datasets, build predictive models, and share notebooks on Kaggle. Explore my other exploratory data analyses and competition entries.
              </p>
            </div>
            
            <a
              href="https://www.kaggle.com/georgeokelloouma"
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
            </a>
          </div>
        </motion.div>
      </div>
    </div>
  );
}
"""

content = content.replace("      </div>\n    </div>\n  );\n}", kaggle_banner)

with open('src/components/PublicationsList.tsx', 'w') as f:
    f.write(content)

