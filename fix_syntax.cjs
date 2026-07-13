const fs = require('fs');

let content = fs.readFileSync('src/App.tsx', 'utf8');

const regex = /const TITLES = \[[\s\S]*?function OscillatingTitle\(\) \{[\s\S]*?\n\}/;
const newCode = `const TITLES = [
  "RESEARCHER",
  "AI & MLOPS\\nENGINEER"
];

function OscillatingTitle() {
  const [index, setIndex] = React.useState(0);

  React.useEffect(() => {
    const timer = setInterval(() => {
      setIndex((prev) => (prev + 1) % TITLES.length);
    }, 4000);
    return () => clearInterval(timer);
  }, []);

  const lines = TITLES[index].split('\\n');

  return (
    <div className="relative inline-flex overflow-hidden items-center text-[clamp(1.5rem,4vw+1rem,5rem)] leading-[0.9]">
      <AnimatePresence mode="wait">
        <motion.div
          key={index}
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -30 }}
          transition={{ duration: 0.5, ease: "easeInOut" }}
          className="flex flex-col items-start"
        >
          {lines.map((line, i) => (
            <span key={i} className="whitespace-nowrap">{line}</span>
          ))}
        </motion.div>
      </AnimatePresence>
    </div>
  );
}`;

content = content.replace(regex, newCode);

fs.writeFileSync('src/App.tsx', content);
