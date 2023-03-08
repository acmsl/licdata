module.exports = {
  preset: './jest-preset.js',
  testEnvironment: 'jest-environment-jsdom',
  transform: {
    '^.+.tsx?$': 'babel-jest',
  },
  setupFilesAfterEnv: ['jest-extended', 'jest-chain', '@testing-library/jest-dom/extend-expect'],
};
