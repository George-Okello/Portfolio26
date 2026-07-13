import React, { useState, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Terminal as TerminalIcon,
  X,
  Maximize2,
  Minimize2,
} from "lucide-react";
import { personalInfo, projects, publications } from "../data";

interface TerminalOverlayProps {
  isDark: boolean;
}

export default function TerminalOverlay({ isDark }: TerminalOverlayProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);
  const [history, setHistory] = useState<
    { command: string; response: string | React.ReactNode }[]
  >([
    {
      command: "",
      response:
        "AI/MLOps Kernel v2.4.1\nType 'help' to see available commands.",
    },
  ]);
  const [input, setInput] = useState("");
  const endRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Toggle terminal on 'ctrl+`' or 'ctrl+\\'
      if (e.ctrlKey && (e.key === "`" || e.key === "\\")) {
        setIsOpen((prev) => !prev);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 100);
      endRef.current?.scrollIntoView({ behavior: "smooth" });
    }
  }, [isOpen, history]);

  const handleCommand = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const cmd = input.trim().toLowerCase();
    let response: string | React.ReactNode = "";

    switch (cmd) {
      case "help":
        response =
          "Available commands:\n- whoami\n- projects\n- publications\n- contact\n- clear";
        break;
      case "whoami":
        response = `Name: ${personalInfo.name}\nRole: ${personalInfo.title}\nBio: ${personalInfo.bio}`;
        break;
      case "projects":
        response = (
          <div className="flex flex-col gap-2">
            {projects.slice(0, 3).map((p) => (
              <div key={p.id}>
                &gt; {p.title} ({p.category})
              </div>
            ))}
            <div>...and more. Type 'publications' for research.</div>
          </div>
        );
        break;
      case "publications":
        response = (
          <div className="flex flex-col gap-2">
            {publications.slice(0, 3).map((p) => (
              <div key={p.id}>&gt; {p.title}</div>
            ))}
          </div>
        );
        break;
      case "contact":
        response = `Email: ${personalInfo.email}\nWebsite: ${personalInfo.website}`;
        break;
      case "clear":
        setHistory([]);
        setInput("");
        return;
      default:
        response = `Command not found: ${cmd}`;
    }

    setHistory((prev) => [...prev, { command: input, response }]);
    setInput("");
  };

  return (
    <>
      <button
        onClick={() => setIsOpen(true)}
        className={`fixed bottom-8 left-8 z-50 p-3 rounded-full shadow-lg border transition-colors flex items-center justify-center ${
          isDark
            ? "bg-[#0B0F19] border-white/20 text-white hover:bg-white hover:text-black"
            : "bg-[#FAFAF9] border-black/20 text-black hover:bg-black hover:text-white"
        }`}
        aria-label="Open Terminal"
      >
        <TerminalIcon className="w-5 h-5" />
      </button>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: 50, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 50, scale: 0.95 }}
            transition={{ type: "spring", stiffness: 300, damping: 25 }}
            className={`fixed z-[100] overflow-hidden border shadow-2xl flex flex-col font-mono text-sm ${
              isExpanded
                ? "inset-4 md:inset-10 rounded-xl"
                : "bottom-24 left-4 md:left-8 w-[calc(100vw-2rem)] md:w-[500px] h-[400px] rounded-lg"
            } ${
              isDark
                ? "bg-[#0B0F19]/95 border-white/10 text-emerald-400 backdrop-blur-xl"
                : "bg-white/95 border-black/10 text-blue-600 backdrop-blur-xl"
            }`}
          >
            {/* Terminal Header */}
            <div
              className={`flex items-center justify-between px-4 py-2 border-b ${isDark ? "border-white/10 bg-white/5" : "border-black/10 bg-black/5"}`}
            >
              <div className="flex items-center gap-2 text-xs font-sans tracking-widest uppercase opacity-70">
                <TerminalIcon className="w-3 h-3" />
                <span>System Terminal</span>
              </div>
              <div className="flex items-center gap-3">
                <button
                  onClick={() => setIsExpanded(!isExpanded)}
                  className="opacity-50 hover:opacity-100 transition-opacity"
                >
                  {isExpanded ? (
                    <Minimize2 className="w-3 h-3" />
                  ) : (
                    <Maximize2 className="w-3 h-3" />
                  )}
                </button>
                <button
                  onClick={() => setIsOpen(false)}
                  className="opacity-50 hover:opacity-100 transition-opacity"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Terminal Content */}
            <div className="flex-1 overflow-y-auto p-4 space-y-4">
              {history.map((entry, i) => (
                <div key={i} className="space-y-1">
                  {entry.command && (
                    <div className="flex gap-2">
                      <span className="opacity-50">root@george:~#</span>
                      <span className={isDark ? "text-white" : "text-black"}>
                        {entry.command}
                      </span>
                    </div>
                  )}
                  {entry.response && (
                    <div className="whitespace-pre-wrap opacity-90">
                      {entry.response}
                    </div>
                  )}
                </div>
              ))}
              <form
                onSubmit={handleCommand}
                className="flex gap-2 items-center"
              >
                <span className="opacity-50">root@george:~#</span>
                <input
                  ref={inputRef}
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  className="flex-1 bg-transparent outline-none focus:ring-0"
                  autoFocus
                  autoComplete="off"
                  spellCheck="false"
                />
              </form>
              <div ref={endRef} />
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
