import React, { useState } from 'react';
import { User, Cpu, Shield, HelpCircle, Bell, Database } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const SettingsPanel: React.FC = () => {
  const [activeTab, setActiveTab] = useState('General');

  const tabs = [
    { name: 'General', icon: User },
    { name: 'AI Config', icon: Cpu },
    { name: 'Rules', icon: Shield },
    { name: 'Storage', icon: Database },
    { name: 'Notifications', icon: Bell },
  ];

  return (
    <div className="bg-white rounded-3xl shadow-2xl border border-gray-100 flex overflow-hidden min-h-[500px]">
      {/* Settings Navigation */}
      <div className="w-64 bg-gray-50 border-r border-gray-100 p-6">
        <h3 className="text-xl font-black text-dark mb-8 px-2">Settings</h3>
        <nav className="space-y-1">
          {tabs.map(tab => (
            <button
              key={tab.name}
              onClick={() => setActiveTab(tab.name)}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-sm transition-all ${
                activeTab === tab.name ? 'bg-white text-primary shadow-sm' : 'text-gray-400 hover:text-dark hover:bg-gray-100'
              }`}
            >
              <tab.icon size={18} />
              {tab.name}
            </button>
          ))}
        </nav>
      </div>

      {/* Settings Content */}
      <div className="flex-1 p-10">
        <AnimatePresence mode="wait">
          <motion.div
            key={activeTab}
            initial={{ opacity: 0, x: 10 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -10 }}
            className="h-full"
          >
            <h2 className="text-2xl font-black text-dark mb-6">{activeTab}</h2>
            
            {activeTab === 'General' && (
              <div className="space-y-6">
                <div>
                  <label className="text-xs font-black text-gray-300 uppercase tracking-widest mb-2 block">App Name</label>
                  <input className="w-full p-3 bg-gray-50 border-none rounded-xl font-medium" defaultValue="Smart File Organizer Pro" />
                </div>
                <div className="flex items-center justify-between p-4 bg-indigo-50 rounded-2xl border border-indigo-100">
                  <div>
                    <h4 className="font-bold text-primary">Beta Updates</h4>
                    <p className="text-[10px] text-primary/60">Get early access to experimental features.</p>
                  </div>
                  <div className="w-12 h-6 bg-primary rounded-full relative">
                    <div className="absolute right-1 top-1 w-4 h-4 bg-white rounded-full" />
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'AI Config' && (
              <div className="space-y-6 text-gray-400 font-medium italic p-10 text-center border-2 border-dashed rounded-3xl border-gray-100">
                AI Configuration options coming soon...
              </div>
            )}
          </motion.div>
        </AnimatePresence>
      </div>
    </div>
  );
};

export default SettingsPanel;
