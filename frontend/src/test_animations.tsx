import { motion } from 'framer-motion';
import { slideInUp, hoverScale, springTransition } from './utils/animations';

export const TestAnimations = () => {
  return (
    <div className="p-20 flex gap-4">
      <motion.div 
        variants={slideInUp}
        initial="initial"
        animate="animate"
        transition={springTransition}
        className="w-20 h-20 bg-primary rounded-xl"
      />
      <motion.button
        {...hoverScale}
        className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-bold"
      >
        Hover Me
      </motion.button>
    </div>
  );
};
