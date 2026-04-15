import AIPreview from './components/AIPreview';

// Simple test for the AI Preview UI
export const TestAIPreview = () => {
  const dummyResult = {
    category: "Finances",
    tags: ["Invoice", "Starbucks", "Coffee"],
    suggested_folder: "Taxes/Receipts",
    confidence: 0.95
  };

  return (
    <div className="p-10 bg-gray-50 min-h-screen">
      <AIPreview result={dummyResult} fileName="starbucks_receipt.pdf" />
    </div>
  );
};
