#!/usr/bin/env node
// Keep .claude-plugin/plugin.json's version in step with package.json.
//   node scripts/sync-plugin-version.mjs          write the version if it differs
//   node scripts/sync-plugin-version.mjs --check  exit 1 if they differ, change nothing
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repo = join(dirname(fileURLToPath(import.meta.url)), "..");
const pkgPath = join(repo, "package.json");
const pluginPath = join(repo, ".claude-plugin", "plugin.json");

const version = JSON.parse(readFileSync(pkgPath, "utf8")).version;
const raw = readFileSync(pluginPath, "utf8");
const current = JSON.parse(raw).version;

if (current === version) {
  console.log(`plugin.json already at ${version}`);
  process.exit(0);
}
if (process.argv.includes("--check")) {
  console.error(`plugin.json is ${current}, package.json is ${version}. Run: npm run sync-plugin-version`);
  process.exit(1);
}
const next = raw.replace(/("version"\s*:\s*")[^"]*(")/, `$1${version}$2`);
if (JSON.parse(next).version !== version) {
  console.error("Could not find a version field in plugin.json");
  process.exit(1);
}
writeFileSync(pluginPath, next);
console.log(`plugin.json ${current} -> ${version}`);
