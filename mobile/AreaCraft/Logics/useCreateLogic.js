import { useState, useEffect } from "react";

const useCreateLogic = (token) => {
  const [employeeData, setEmployeeData] = useState(null);
  const [employeeImage, setEmployeeImage] = useState(null);

  return { employeeData, employeeImage };
};

export default useCreateLogic;
