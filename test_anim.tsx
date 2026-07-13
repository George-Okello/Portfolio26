import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const TITLES = [
  "RESEARCHER",
  "MACHINE LEARNING ENGINEER",
  "DATA SCIENTIST",
  "AI RESEARCHER"
];

export function OscillatingTitle() {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setIndex((prev) => (prev + 1) % TITLES.length);
    }, 3000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="relative inline-flex overflow-hidden items-center" style={{ minWidth: '8ch' }}>
      <AnimatePresence mode="wait">
        <motion.span
          key={index}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          transition={{ duration: 0.4, ease: "easeInOut" }}
          className="inline-block whitespace-nowrap"
        >
          {TITLES[index]}
        </motion.span>
      </AnimatePresence>
    </div>
  );
}
