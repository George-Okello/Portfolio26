import { motion, useScroll, useTransform } from "motion/react";
import React, { useRef } from "react";

export function RevealWrapper({
  children,
  className = "",
}: {
  children: React.ReactNode;
  className?: string;
}) {
  const ref = useRef<HTMLDivElement>(null);

  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });

  const opacity = useTransform(scrollYProgress, [0, 0.1, 0.9, 1], [0, 1, 1, 0]);
  const scale = useTransform(
    scrollYProgress,
    [0, 0.1, 0.9, 1],
    [0.95, 1, 1, 0.95],
  );
  const filter = useTransform(
    scrollYProgress,
    [0, 0.1, 0.9, 1],
    ["blur(10px)", "blur(0px)", "blur(0px)", "blur(10px)"],
  );

  return (
    <motion.div
      ref={ref}
      style={{ opacity, scale, filter }}
      className={className}
    >
      {children}
    </motion.div>
  );
}
