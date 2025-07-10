function DebugLogin() {
  return (
    <form onSubmit={(e) => {
      e.preventDefault();
      alert("Submitted!");
    }}>
      <button type="submit">Test Submit</button>
    </form>
  );
}
