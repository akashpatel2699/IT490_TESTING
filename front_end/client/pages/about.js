import Head from "next/head";

import axios from "axios";

import React, { useEffect, useState } from "react";

const about = () => {
  const [employees, setEmployees] = useState([]);
  let tmp = "http://dummy.restapiexample.com/api/v1/employees";

  useEffect(() => {
    axios
      .get("/api/users")
      .then((res) => {
        console.log(res);
        // setEmployees(data.data);
        // console.log(employees)
      }).catch( err => {
          console.log(err)
      });
  }, []);

  return (
    <>
      <Head>
        <title>About Page</title>
      </Head>
      <div>
        <h1>This is about page! Welcome!</h1>
        <ul>
          {employees &&
            employees.map((value, index) => 
              <li key={index}>{value.employee_name}</li>
            )}
        </ul>
      </div>
    </>
  );
};

export default about;
