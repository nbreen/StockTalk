import { Injectable } from '@angular/core';
import { User } from '../app/user';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { isPrivateIdentifier } from 'typescript';
 
@Injectable({
  providedIn: 'root'
})

export class CrudService {

  readonly APIUrl = "http://127.0.0.1:8000";
  
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }
  
  constructor(private httpClient: HttpClient) { }

  getAllUsers(): Observable<User> {
    return this.httpClient.get<User>(this.APIUrl + "/user/")
    
    /*
    .pipe(
      catchError(this.handleError<User>('getAllUsers'))
    )
    */
    
  }

  addUser(val:any) {

      let body = JSON.stringify(val);
      return this.httpClient.post<any>(this.APIUrl + "/user/", body);

      /*
      .pipe(
        catchError(this.handleError<User>('createUser'))
      );
      */
  }

  getUserById(id) : Observable<User> {
    return this.httpClient.get<User>(this.APIUrl + "/user/")

    /*
    .pipe(
      catchError(this.handleError<User>('getUserById'))
    );
    */
  }

  

  updateUser(id, user): Observable<User> {
    return this.httpClient.put<User>(this.APIUrl + "/user/", JSON.stringify(user), this.httpOptions)

    /*
    .pipe(
      catchError(this.handleError<User>('updateUser'))
    );
    */

  }

  deleteUser(id): Observable<User> {
    return this.httpClient.delete<User>(this.APIUrl + "/user/", this.httpOptions)

    /*
    .pipe(
      catchError(this.handleError<User>('deleteUser'))
    )
    */
   
  }

  /* need create read update delete for 
  
    Interation
    comment
    Post
    Topic
    User
  
  */

  /** Message service for loggin success of crud operations */
  /*private log(message: string) {
    this.messageService.add(`HeroService: ${message}`);
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */

  private handleError<T>(operation = 'operation', result?: T) {
      // TODO: send the error to remote logging infrastructure
      console.log(operation); // log to console instead
  };
}
