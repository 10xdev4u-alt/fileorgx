import { useKeyboardShortcuts } from './hooks/useKeyboardShortcuts';

export const TestShortcuts = () => {
  useKeyboardShortcuts({
    'Ctrl+Shift+O': () => alert('Organize triggered!'),
    '/': () => console.log('Search focused'),
    'Escape': () => console.log('Menu closed')
  });

  return (
    <div className="p-20">
      <h2 className="text-xl font-bold">Keyboard Shortcuts Active</h2>
      <ul className="mt-4 list-disc pl-5">
        <li>Ctrl+Shift+O: Alert</li>
        <li>/: Console log</li>
        <li>Escape: Console log</li>
      </ul>
    </div>
  );
};
