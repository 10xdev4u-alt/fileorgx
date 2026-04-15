import React, { useState } from 'react';
import { Search, Filter, X, ChevronDown, Calendar, FileType } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { scaleUp } from '../utils/animations';

const SearchBar: React.FC = () => {
  const [isFilterOpen, setIsFilterOpen] = useState(false);
  const [query, setQuery] = useState("");

  const clearQuery = () => setQuery("");

  return (
    <div className="relative w-full max-w-2xl mx-auto">
      <div className="relative group">
        <Search className="absolute left-5 top-1/2 -translate-y-1/2 text-gray-400 group-hover:text-primary transition-colors" size={20} />
        <input 
          placeholder="Search by name, tag, or content..." 
          className="w-full pl-14 pr-24 py-4 bg-white border border-gray-100 rounded-3xl shadow-lg shadow-gray-100 focus:ring-4 focus:ring-primary/10 focus:border-primary/30 transition-all text-dark font-medium outline-none"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <div className="absolute right-4 top-1/2 -translate-y-1/2 flex items-center gap-2">
          {query && (
            <button onClick={clearQuery} className="p-1 hover:bg-gray-100 rounded-lg text-gray-400">
              <X size={16} />
            </button>
          )}
          <button 
            onClick={() => setIsFilterOpen(!isFilterOpen)}
            className={`p-2 rounded-xl transition-all ${isFilterOpen ? 'bg-primary text-white shadow-lg shadow-indigo-100' : 'bg-gray-50 text-gray-400 hover:bg-gray-100'}`}
          >
            <Filter size={20} />
          </button>
        </div>
      </div>

      <AnimatePresence>
        {isFilterOpen && (
          <motion.div
            {...scaleUp}
            className="absolute top-20 left-0 right-0 bg-white rounded-3xl p-8 shadow-2xl border border-gray-100 z-50 origin-top"
          >
            <div className="grid grid-cols-2 gap-8">
              <div>
                <label className="text-xs font-black text-gray-300 uppercase tracking-widest flex items-center gap-2 mb-4">
                  <FileType size={14} />
                  File Type
                </label>
                <div className="grid grid-cols-2 gap-2">
                  {['Images', 'PDFs', 'Documents', 'Code'].map(type => (
                    <button key={type} className="px-4 py-2 bg-gray-50 text-gray-500 rounded-xl text-xs font-bold hover:bg-indigo-50 hover:text-primary transition-all">
                      {type}
                    </button>
                  ))}
                </div>
              </div>

              <div>
                <label className="text-xs font-black text-gray-300 uppercase tracking-widest flex items-center gap-2 mb-4">
                  <Calendar size={14} />
                  Date Range
                </label>
                <div className="space-y-2">
                  <button className="w-full px-4 py-2 bg-gray-50 text-gray-500 rounded-xl text-xs font-bold hover:bg-indigo-50 hover:text-primary text-left">
                    All Time
                  </button>
                  <button className="w-full px-4 py-2 bg-gray-50 text-gray-500 rounded-xl text-xs font-bold hover:bg-indigo-50 hover:text-primary text-left">
                    Last 7 Days
                  </button>
                  <button className="w-full px-4 py-2 bg-gray-50 text-gray-500 rounded-xl text-xs font-bold hover:bg-indigo-50 hover:text-primary text-left">
                    Custom...
                  </button>
                </div>
              </div>
            </div>

            <div className="mt-8 pt-6 border-t border-gray-100 flex items-center justify-between">
              <button className="text-xs font-black text-gray-300 hover:text-red-400 uppercase tracking-widest transition-colors">
                Reset Filters
              </button>
              <button className="px-8 py-2 bg-primary text-white rounded-xl font-black text-xs shadow-lg shadow-indigo-100 hover:scale-105 active:scale-95 transition-all">
                Apply Search
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default SearchBar;
