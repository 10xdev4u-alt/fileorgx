import React, { useState } from 'react';
import { Shield, MoreVertical, Edit, Trash2, Power } from 'lucide-react';
import { motion } from 'framer-motion';

interface Rule {
  id: number;
  name: string;
  isActive: boolean;
  condition: string;
  action: string;
}

const RuleListView: React.FC = () => {
  const [rules, setRules] = useState<Rule[]>([
    { id: 1, name: "Screenshot Mover", isActive: true, condition: "name contains 'screenshot'", action: "Move to Images/Screenshots" },
    { id: 2, name: "Invoice Tagger", isActive: true, condition: "content contains 'invoice'", action: "Tag as Finance" },
    { id: 3, name: "Old Log Cleaner", isActive: false, condition: "extension is '.log' and older than 30d", action: "Move to Archive/Logs" },
  ]);

  const toggleRule = (id: number) => {
    setRules(rules.map(r => r.id === id ? { ...r, isActive: !r.isActive } : r));
  };

  return (
    <div className="bg-white rounded-[40px] shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-8 border-b border-gray-50 flex items-center justify-between">
        <h3 className="text-xl font-black text-dark tracking-tight flex items-center gap-3">
          <Shield className="text-primary" />
          Active Rules
        </h3>
        <span className="bg-indigo-50 text-primary px-4 py-1 rounded-full text-xs font-black">
          {rules.filter(r => r.isActive).length} Active
        </span>
      </div>

      <div className="divide-y divide-gray-50">
        {rules.map((rule) => (
          <div key={rule.id} className={`p-6 flex items-center justify-between transition-all ${rule.isActive ? 'bg-white' : 'bg-gray-50/50 opacity-60'}`}>
            <div className="flex items-center gap-6">
              <button 
                onClick={() => toggleRule(rule.id)}
                className={`w-12 h-12 rounded-2xl flex items-center justify-center transition-all ${
                  rule.isActive ? 'bg-primary text-white shadow-lg shadow-indigo-100' : 'bg-gray-200 text-gray-400'
                }`}
              >
                <Power size={20} />
              </button>
              <div>
                <h4 className="font-bold text-dark mb-1">{rule.name}</h4>
                <div className="flex items-center gap-2 text-xs text-gray-400 font-medium">
                  <span className="px-2 py-0.5 bg-gray-100 rounded text-[10px] uppercase font-bold text-gray-500">IF</span>
                  {rule.condition}
                  <span className="px-2 py-0.5 bg-gray-100 rounded text-[10px] uppercase font-bold text-gray-500 ml-2">THEN</span>
                  {rule.action}
                </div>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <button className="p-2 hover:bg-gray-100 rounded-xl text-gray-400 transition-all">
                <Edit size={18} />
              </button>
              <button className="p-2 hover:bg-red-50 rounded-xl text-gray-400 hover:text-red-500 transition-all">
                <Trash2 size={18} />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RuleListView;
