import { useEffect } from 'react';

type ShortcutMap = {
  [key: string]: () => void;
};

export const useKeyboardShortcuts = (shortcuts: ShortcutMap) => {
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      const { key, ctrlKey, shiftKey, altKey, metaKey } = event;
      
      // Build string representation of shortcut
      let keys = [];
      if (ctrlKey) keys.push('Ctrl');
      if (shiftKey) keys.push('Shift');
      if (altKey) keys.push('Alt');
      if (metaKey) keys.push('Meta');
      
      // Handle actual key
      const keyName = key.length === 1 ? key.toUpperCase() : key;
      if (!['Control', 'Shift', 'Alt', 'Meta'].includes(keyName)) {
        keys.push(keyName);
      }
      
      const shortcutStr = keys.join('+');
      
      if (shortcuts[shortcutStr]) {
        event.preventDefault();
        shortcuts[shortcutStr]();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [shortcuts]);
};
