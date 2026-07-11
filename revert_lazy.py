import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace lazy imports with standard imports
lazy_imports = """import { lazy, Suspense } from "react";
const ResearchSandbox = lazy(() => import("./components/ResearchSandbox"));
const PublicationsList = lazy(() => import("./components/PublicationsList"));
const AcademicTimeline = lazy(() => import("./components/AcademicTimeline"));
const EducationSpiral = lazy(() => import("./components/EducationSpiral"));
const GenerativeArt = lazy(() => import("./components/GenerativeArt"));
const TechnicalSkills = lazy(() => import("./components/TechnicalSkills").then(m => ({ default: m.TechnicalSkills })));"""

static_imports = """import ResearchSandbox from "./components/ResearchSandbox";
import PublicationsList from "./components/PublicationsList";
import AcademicTimeline from "./components/AcademicTimeline";
import EducationSpiral from "./components/EducationSpiral";
import GenerativeArt from "./components/GenerativeArt";
import { TechnicalSkills } from "./components/TechnicalSkills";"""

content = content.replace(lazy_imports, static_imports)

# Remove Suspense wrappers
pattern = r'<Suspense fallback=\{<div className="w-full h-32 flex items-center justify-center opacity-50"><div className="animate-pulse">Loading [^<]*</div></div>\}>\s*(<[A-Za-z0-9_]+\s*[^>]*/>)\s*</Suspense>'

content = re.sub(pattern, r'\1', content)

with open('src/App.tsx', 'w') as f:
    f.write(content)

