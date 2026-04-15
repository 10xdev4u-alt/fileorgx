import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Sparkles, Zap, Shield, Rocket, ArrowRight, ArrowLeft } from 'lucide-react';
import { scaleUp, fadeIn } from '../utils/animations';

const steps = [
  {
    title: "Welcome to FileOrgX",
    description: "Your digital life is about to get a whole lot cleaner. Let's show you around!",
    icon: Sparkles,
    color: "bg-indigo-500"
  },
  {
    title: "AI Power",
    description: "Our local AI analyzes your files (OCR, LLM) to understand what they are without them ever leaving your machine.",
    icon: Zap,
    color: "bg-yellow-500"
  },
  {
    title: "Smart Rules",
    description: "Create rules to move, tag, or rename files automatically based on their content or metadata.",
    icon: Shield,
    color: "bg-emerald-500"
  },
  {
    title: "You're Ready!",
    description: "Start by adding a folder to watch and let the magic happen.",
    icon: Rocket,
    color: "bg-primary"
  }
];

const Onboarding: React.FC<{ onComplete: () => void }> = ({ onComplete }) => {
  const [currentStep, setCurrentStep] = useState(0);

  const next = () => {
    if (currentStep < steps.length - 1) setCurrentStep(currentStep + 1);
    else onComplete();
  };

  const prev = () => {
    if (currentStep > 0) setCurrentStep(currentStep - 1);
  };

  const StepIcon = steps[currentStep].icon;

  return (
    <div className="fixed inset-0 z-[100] bg-dark/20 backdrop-blur-xl flex items-center justify-center p-6">
      <motion.div
        {...scaleUp}
        className="bg-white rounded-[40px] shadow-2xl w-full max-w-lg overflow-hidden"
      >
        <div className={`h-40 ${steps[currentStep].color} flex items-center justify-center transition-colors duration-500`}>
          <motion.div
            key={currentStep}
            initial={{ scale: 0, rotate: -20 }}
            animate={{ scale: 1, rotate: 0 }}
            className="w-20 h-20 bg-white/20 rounded-3xl flex items-center justify-center text-white backdrop-blur-md"
          >
            <StepIcon size={40} />
          </motion.div>
        </div>

        <div className="p-12 text-center">
          <AnimatePresence mode="wait">
            <motion.div
              key={currentStep}
              {...fadeIn}
              className="min-h-[120px]"
            >
              <h2 className="text-3xl font-black text-dark mb-4">{steps[currentStep].title}</h2>
              <p className="text-gray-500 leading-relaxed">{steps[currentStep].description}</p>
            </motion.div>
          </AnimatePresence>

          <div className="flex items-center justify-center gap-2 mt-8 mb-12">
            {steps.map((_, idx) => (
              <div 
                key={idx} 
                className={`h-2 rounded-full transition-all duration-300 ${idx === currentStep ? 'w-8 bg-primary' : 'w-2 bg-gray-200'}`}
              />
            ))}
          </div>

          <div className="flex items-center justify-between gap-4">
            <button 
              onClick={prev}
              className={`flex items-center gap-2 font-bold text-gray-400 hover:text-dark transition-all ${currentStep === 0 ? 'opacity-0 pointer-events-none' : ''}`}
            >
              <ArrowLeft size={18} />
              Back
            </button>
            <button 
              onClick={next}
              className="flex items-center gap-2 px-8 py-3 bg-primary text-white rounded-2xl font-black shadow-lg shadow-indigo-100 hover:scale-105 active:scale-95 transition-all"
            >
              {currentStep === steps.length - 1 ? 'Get Started' : 'Next'}
              <ArrowRight size={18} />
            </button>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default Onboarding;
