import React from 'react';
import { Search, Settings, Moon, Sun, Plus, Zap, History, LayoutDashboard } from 'lucide-react';

const Dashboard: React.FC = () => {
  return (
    <div className="flex h-screen bg-gray-50 text-dark font-sans">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-gray-100 p-6 flex flex-col gap-8">
        <div className="flex items-center gap-3 px-2">
          <div className="w-8 h-8 bg-primary rounded-lg flex items-center justify-center text-white font-black">S</div>
          <span className="font-black text-xl tracking-tight">FileOrg<span className="text-primary">X</span></span>
        </div>

        <nav className="flex flex-col gap-2">
          <button className="flex items-center gap-3 px-4 py-3 bg-indigo-50 text-primary rounded-xl font-bold transition-all">
            <LayoutDashboard size={20} />
            Dashboard
          </button>
          <button className="flex items-center gap-3 px-4 py-3 text-gray-400 hover:bg-gray-50 hover:text-dark rounded-xl font-medium transition-all">
            <History size={20} />
            History
          </button>
          <button className="flex items-center gap-3 px-4 py-3 text-gray-400 hover:bg-gray-50 hover:text-dark rounded-xl font-medium transition-all">
            <Settings size={20} />
            Settings
          </button>
        </nav>

        <div className="mt-auto">
          <div className="bg-indigo-600 rounded-2xl p-5 text-white shadow-lg shadow-indigo-200">
            <Zap size={24} className="mb-3 text-yellow-300 fill-yellow-300" />
            <h4 className="font-bold text-sm mb-1">Go Pro</h4>
            <p className="text-[10px] opacity-80 mb-4">Unlock advanced AI analysis and bulk actions.</p>
            <button className="w-full bg-white text-primary py-2 rounded-xl text-xs font-black">Upgrade Now</button>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <header className="h-20 bg-white border-b border-gray-100 flex items-center justify-between px-10 shrink-0">
          <div className="relative w-96">
            <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" size={18} />
            <input 
              placeholder="Find that pizza receipt..." 
              className="w-full pl-12 pr-4 py-2.5 bg-gray-50 border-none rounded-2xl text-sm focus:ring-2 focus:ring-primary/20 transition-all"
            />
          </div>

          <div className="flex items-center gap-4">
            <button className="p-2.5 bg-gray-50 text-gray-500 rounded-2xl hover:bg-gray-100 transition-all">
              <Moon size={20} />
            </button>
            <div className="w-10 h-10 bg-indigo-100 rounded-2xl overflow-hidden border-2 border-white shadow-sm">
              <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix" alt="User" />
            </div>
          </div>
        </header>

        {/* Scrollable Area */}
        <div className="flex-1 overflow-auto p-10">
          <div className="flex items-center justify-between mb-8">
            <h1 className="text-3xl font-black text-dark tracking-tight">Overview</h1>
            <button className="flex items-center gap-2 bg-primary text-white px-6 py-3 rounded-2xl font-black shadow-lg shadow-indigo-200 hover:scale-105 active:scale-95 transition-all">
              <Plus size={20} />
              Organize Now
            </button>
          </div>

          <div className="grid grid-cols-3 gap-8">
            {/* Stats Cards Placeholder */}
            <div className="bg-white p-6 rounded-3xl border border-gray-100 shadow-sm">
              <span className="text-xs font-bold text-gray-400 uppercase tracking-widest">Organized Files</span>
              <div className="text-4xl font-black text-dark mt-2">1,284</div>
            </div>
            <div className="bg-white p-6 rounded-3xl border border-gray-100 shadow-sm">
              <span className="text-xs font-bold text-gray-400 uppercase tracking-widest">Storage Saved</span>
              <div className="text-4xl font-black text-success mt-2">12.4GB</div>
            </div>
            <div className="bg-white p-6 rounded-3xl border border-gray-100 shadow-sm">
              <span className="text-xs font-bold text-gray-400 uppercase tracking-widest">Rules Active</span>
              <div className="text-4xl font-black text-primary mt-2">18</div>
            </div>
          </div>
          
          {/* Timeline Placeholder will go here */}
          <div className="mt-12 h-64 bg-white rounded-3xl border border-gray-100 border-dashed flex items-center justify-center text-gray-300 font-bold italic">
            Visual Timeline Coming Soon...
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
