import React from 'react';
import { Moon, Sun } from 'lucide-react';
import { useDarkMode } from '../hooks/useDarkMode';
import { motion } from 'framer-motion';

const ThemeToggle: React.FC = () => {
  const { isDark, toggleDarkMode } = useDarkMode();

  return (
    <motion.button
      whileTap={{ scale: 0.9 }}
      onClick={toggleDarkMode}
      className="p-2.5 bg-gray-50 dark:bg-zinc-900 text-gray-500 dark:text-zinc-400 rounded-2xl hover:bg-gray-100 dark:hover:bg-zinc-800 transition-all border border-transparent dark:border-zinc-800 shadow-sm"
    >
      {isDark ? <Sun size={20} className="text-yellow-400" /> : <Moon size={20} />}
    </motion.button>
  );
};

export default ThemeToggle;
