import React, { useState } from 'react';
import { Plus, Trash2, ArrowUpDown, Save } from 'lucide-react';

interface Rule {
  id?: number;
  name: string;
  condition_type: string;
  condition_value: string;
  action_type: string;
  action_value: string;
  priority: number;
}

const RuleBuilder: React.FC = () => {
  const [rules, setRules] = useState<Rule[]>([]);
  const [newRule, setNewRule] = useState<Rule>({
    name: '',
    condition_type: 'extension',
    condition_value: '',
    action_type: 'move',
    action_value: '',
    priority: 0
  });

  const addRule = () => {
    setRules([...rules, { ...newRule, id: Date.now() }]);
    setNewRule({
      name: '',
      condition_type: 'extension',
      condition_value: '',
      action_type: 'move',
      action_value: '',
      priority: 0
    });
  };

  const deleteRule = (id: number) => {
    setRules(rules.filter(r => r.id !== id));
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow-md">
      <h2 className="text-xl font-bold mb-6 flex items-center gap-2">
        <ArrowUpDown className="text-primary" />
        Organization Rules
      </h2>

      {/* New Rule Form */}
      <div className="grid grid-cols-2 gap-4 bg-gray-50 p-4 rounded-lg mb-8">
        <input 
          placeholder="Rule Name"
          className="p-2 border rounded"
          value={newRule.name}
          onChange={e => setNewRule({...newRule, name: e.target.value})}
        />
        <select 
          className="p-2 border rounded"
          value={newRule.condition_type}
          onChange={e => setNewRule({...newRule, condition_type: e.target.value})}
        >
          <option value="extension">File Extension</option>
          <option value="filename_contains">Filename Contains</option>
          <option value="size_greater_than">Size Greater Than</option>
        </select>
        <input 
          placeholder="Condition Value"
          className="p-2 border rounded"
          value={newRule.condition_value}
          onChange={e => setNewRule({...newRule, condition_value: e.target.value})}
        />
        <input 
          placeholder="Target Folder/Tag"
          className="p-2 border rounded"
          value={newRule.action_value}
          onChange={e => setNewRule({...newRule, action_value: e.target.value})}
        />
        <button 
          onClick={addRule}
          className="col-span-2 bg-primary text-white py-2 rounded-lg font-bold flex items-center justify-center gap-2 hover:bg-opacity-90"
        >
          <Plus size={20} /> Add Rule
        </button>
      </div>

      {/* Rules List */}
      <div className="space-y-3">
        {rules.map(rule => (
          <div key={rule.id} className="flex items-center justify-between p-4 border rounded-lg hover:border-primary transition-all group">
            <div className="flex-1">
              <h4 className="font-bold text-dark">{rule.name}</h4>
              <p className="text-sm text-gray-500">
                If {rule.condition_type} is "{rule.condition_value}" then {rule.action_type} to "{rule.action_value}"
              </p>
            </div>
            <button 
              onClick={() => deleteRule(rule.id!)}
              className="text-gray-400 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-all"
            >
              <Trash2 size={20} />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RuleBuilder;
